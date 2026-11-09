---
name: web-security-review
description: Yapada sitelerinin ve her yeni web uygulamasının (Cloudflare Workers, Durable Objects, D1, statik sayfa, PWA, GitHub Actions ile yayın, Windows ajanı) güvenlik incelemesi. Yeni site/endpoint yazarken, giriş/oturum/PIN/token koduna dokunurken, müşteri verisi (telefon, ad) işlerken, wrangler.jsonc veya _headers veya workflow değiştirirken ve HER canlı yayından önce kullan. "güvenlik", "güvenli mi", "açık var mı", "tara", "yayına almadan önce" gibi ifadelerde mutlaka tetiklenir.
metadata:
  origin: "affaan-m/everything-claude-code v2.2.3 (MIT) — agents/security-reviewer.md, skills/security-review, rules/web/security.md; Yapada yığınına uyarlandı"
---

# Web Güvenlik İncelemesi (Yapada yığını)

ECC'nin `security-reviewer` ajanı ve `security-review` skill'indeki OWASP kontrol listesinin, kullanıcının gerçek altyapısına uyarlanmış hâli. ECC örnekleri Next.js/Supabase/Express odaklıdır; burada karşılıkları Cloudflare Workers dünyasına çevrildi ve 2026-11-09 denetiminde bulunan gerçek hatalardan çıkan dersler eklendi.

## Ne zaman

- **Her zaman:** yeni `/api/*` route, giriş/oturum/PIN/token kodu, müşteri verisi, dosya içe/dışa aktarma, harici API (Drive, iCloud, WhatsApp/Meta), `wrangler.jsonc`, `_headers`, `.github/workflows/*` değişikliği.
- **Hemen:** canlı yayından önce, bağımlılık güncellemesinden sonra, kullanıcı "güvenli mi" diye sorduğunda.

## Nasıl çalışılır

1. **Otomatik taramalar** (her depoda):
   ```bash
   npm audit --omit=dev            # üretim bağımlılıkları; 0 olmalı
   npm audit                       # geliştirme araçları; HIGH varsa güncelle
   git log -p --all | grep -E -i 'AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_|github_pat_|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE'
   git log --all --diff-filter=A --name-only --format= | grep -i -E '\.env|token\.txt|\.dev\.vars|\.pem|\.key$'
   ```
2. **Elle inceleme**: aşağıdaki kontrol listesini route route uygula. Büyük depolarda her depo için ayrı, salt-okur bir alt ajan çalıştır; ajana bu dosyayı kontrol listesi olarak ver, bulguları dosya:satır ile iste.
3. **Doğrula**: CRITICAL/HIGH her bulguyu kodu kendin okuyarak teyit et (ajan raporu tek başına yeterli değil).
4. **Rapor**: önem (CRITICAL/HIGH/MEDIUM/LOW), dosya:satır, nasıl istismar edilir, en küçük düzeltme. Sağlam bulunanları da kısaca yaz.
5. **Düzeltme**: Canlı yayın, secret/PIN değişimi ve `main`'e push kullanıcının açık onayı olmadan yapılmaz (depo AGENTS.md kuralı). Düzeltmeyi ayrı dalda hazırla, onay iste.

## Kontrol listesi

### 1. Kimlik doğrulama ve oturum
- [ ] `login`, `logout`, `status` dışındaki **her** `/api/*` route oturum istiyor mu? Yönetici route'ları rol kontrolü yapıyor mu?
- [ ] PIN/şifre: **varsayılan veya ortak değer yok** (ör. herkese `1234` → CRITICAL). Yönetici hesabı en az 8 haneli/ayrı güçlü sır.
- [ ] PIN/şifre özetleri `wrangler.jsonc` `vars` içinde **değil**, `wrangler secret put` ile. `vars` git'e girer; 4–6 haneli PIN'in PBKDF2 özeti çevrimdışı saniyeler içinde kırılır.
- [ ] Karşılaştırma sabit zamanlı; olmayan hesapta da aynı iş yapılıyor.
- [ ] Deneme sınırı: IP başına **ve** hesap başına; ama hesap kilidi doğru PIN'i de engelliyorsa saldırgan şubeyi kilitleyebilir (DoS) → kilidi hesap+IP'ye bağla veya doğru PIN'i geçir. IPv6'da /64 bazında say. Sayaç kayıtlarının süresi dolsun.
- [ ] Ek katman olarak Cloudflare WAF rate-limit kuralı: `/api/login`, `/api/admin/login`, herkese açık arama uçları.
- [ ] Çerez: `__Host-` önekli, `Secure; HttpOnly; SameSite=Lax|Strict`; token rastgele ≥ 128 bit, sunucuda yalnızca SHA-256 özeti. Girişte eski oturum silinir. Ömür makul (90 gün fazla; boşta kalma süresi ekle).
- [ ] Makine-makine token (ör. fiyatgör ajanı): ≥ 32 karakter `openssl rand -hex 32`, sunucu da ≥ 32'yi zorlasın; sabit zamanlı karşılaştırma.

### 2. Yetkilendirme (IDOR)
- [ ] Şube kullanıcısı başka şubenin kaydını **okuyamıyor ve yazamıyor**: her sorgu `visible`/`branchId` ile süzülüyor; `?branch=` ile kapsam genişlemiyor.
- [ ] Telefon/müşteri gibi şube-üstü kayıtlarda bile kullanıcıya görünür sipariş yoksa 404.
- [ ] İstemciden gelen alanlar (`source`, `personnelName`, rol) güvenilmiyor; beyaz liste + oturumdaki kimlikle eşleştirme.

### 3. CSRF ve istek doğrulama
- [ ] Durum değiştiren her istek **POST** (GET ile token döndürme, kayıt silme, harici API çağırma yok).
- [ ] POST'larda: tam `Origin` eşleşmesi (`APP_ORIGIN`), özel başlık (`X-Yapada-Request: 1`), `content-type: application/json`, gövde boyut sınırı ve okuma zaman aşımı. Yeni projede `worker/request.ts` desenini kopyala.

### 4. Enjeksiyon
- [ ] D1/DO SQLite: değerler daima `?` ile bağlanır; SQL metnine yalnızca sabit sütun adları/yer tutucu listeleri girer.
- [ ] CSV/Excel dışa aktarma: `=`, `+`, `-`, `@`, sekme, CR ile başlayan hücrelerin başına `'` (formül enjeksiyonu). Sunucu ve **istemci** tarafı CSV'lerin ikisi de.
- [ ] PowerShell/ajan: harici veriyle komut kurulmuyor; ODBC sorguları parametreli.

### 5. XSS ve CSP
- [ ] `innerHTML` yalnızca `esc()` ile kaçırılmış veriyle; tercihen `textContent`.
- [ ] CSP her yanıtta: `default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'`. `script-src 'unsafe-inline'` yok — satır içi betik gerekiyorsa `'sha256-…'` özeti veya ayrı dosya. `'wasm-unsafe-eval'` yalnızca WASM gerçekten varsa.
- [ ] Üçüncü taraf betik/CDN yok; zorunluysa SRI + sabit sürüm.
- [ ] Bağlantılar: `target="_blank"` → `rel="noopener"`; `wa.me` bağlantıları rakam + `encodeURIComponent` ile.

### 6. Güvenlik başlıkları (`_headers` veya Worker yanıtı)
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer   (veya strict-origin-when-cross-origin)
Permissions-Policy: camera=(), microphone=(), geolocation=()   (barkod okuyucuda camera=(self))
X-Robots-Tag: noindex          (iç panellerde)
Cache-Control: no-store        (/api/* yanıtlarında)
```
- [ ] CORS başlığı yok (yalnız aynı köken) — gerekiyorsa tek köken, `*` asla.

### 7. Cloudflare yapılandırması
- [ ] `workers_dev: false` ve `preview_urls: false` (özel alan adı varken `*.workers.dev` ikinci bir kapı açar; Cloudflare Access kullanılırsa onu **atlatır**).
- [ ] Sırlar `wrangler secret`; `vars` yalnızca gizli olmayan ayarlar. `account_id`/`zone_id` sır değildir.
- [ ] Durable Object tek kuyrukta çalışıyorsa, kimlik doğrulamasız istekler (login seli) kuyruğa girmeden önce sınırlanmalı.
- [ ] Hata yanıtları genel mesaj; ayrıntı yalnız log'da (veya geçerli token'la).

### 8. PWA / Service Worker
- [ ] `/api/` önbelleğe alınmıyor.
- [ ] Yalnızca `response.ok` olan yanıtlar önbelleğe yazılıyor (404/5xx kalıcı olarak servis edilmesin).
- [ ] Önbellek sürümü her yayında değişiyor.

### 9. GitHub Actions
- [ ] `permissions: contents: read` (en üstte).
- [ ] `pull_request` işlerinde **hiçbir secret yok** (ör. `wrangler whoami` adımına `CLOUDFLARE_API_TOKEN` vermek, PR'daki değiştirilmiş `package-lock`/betiklerle token'ı sızdırabilir). Secret yalnızca `push`→`main` veya `workflow_dispatch` işinde, mümkünse onaylı `environment` ile.
- [ ] `pull_request_target` kullanma; `run:` içinde `${{ github.event.* }}` gibi güvenilmeyen girdi yok.
- [ ] Action'lar commit SHA'ya sabit (`actions/checkout@<sha> # v4`); `npx wrangler@4` yerine kilit dosyasından veya tam sürüm.

### 10. Mağaza bilgisayarındaki ajanlar (Windows)
- [ ] Ajan klasörü yalnızca o kullanıcı + SYSTEM + Administrators yazabilir: `icacls <dizin> /inheritance:r /grant:r "%USERNAME%:(OI)(CI)F" "SYSTEM:(OI)(CI)F" "Administrators:(OI)(CI)F"`. Aksi hâlde `-ExecutionPolicy Bypass` ile çalışan zamanlanmış görev başka kullanıcıya kod çalıştırma kapısı olur.
- [ ] Token düz metin dosyada değil (DPAPI: `ConvertTo-SecureString`/`Export-Clixml`); ZIP paketinin içinde gönderilmez, ayrı kanaldan verilir.
- [ ] Sunucu adresi sabit `https://…yapadakirtasiye.com`; ayar dosyasından gelen başka adrese token gönderilmez.
- [ ] Zamanlanmış görev SYSTEM/yönetici değil, sınırlı kullanıcıyla.

### 11. Kişisel veri (KVKK)
- [ ] Müşteri telefonu/adı yalnız yetkili oturumla; dışa aktarma yalnız yönetici.
- [ ] Herkese açık sayfalarda kişisel cep numarası/ev adresi var mı — kullanıcıya sor.
- [ ] Log'larda telefon, PIN, token yok.

## Rapor şablonu

```
## <depo> — <tarih>
Otomatik: npm audit (prod) X | geçmişte sır: yok/var | canlı başlık kontrolü: yapıldı/ağ engelli
| Önem | Dosya:satır | Sorun | İstismar | Düzeltme |
Sağlam bulunanlar: …
```
Raporu `SECURITY-AUDIT-<YYYY-MM-DD>.md` olarak kullanıcıya dosya hâlinde ver. **Ayrıntılı bulguları herkese açık depoya (`ogulcaners/claude` public) asla commit etme** — yalnızca özel (private) bir depoya, kullanıcı onayıyla.
