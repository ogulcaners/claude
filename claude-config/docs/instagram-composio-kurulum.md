# Instagram'ı Claude'a Bağlama Rehberi (Composio köprüsü)

Kaynak: "Instagram'ı Claude'a bağla: analiz, içerik planı ve DM taslakları" (Yedi AI, ücretsiz rehber, 05.11.2026) + bu depodaki çalışma kuralları. Arayüzler zamanla değişebilir; takılırsan Composio'nun güncel sayfasına bak.

## 0. Ön koşullar (5 dk)

| # | Gerekli | Nasıl |
|---|---|---|
| 1 | **Profesyonel Instagram hesabı** (Business veya Creator) | Instagram → Ayarlar → Hesap türü ve araçlar → Profesyonel hesaba geç. Kişisel hesapla bağlayıcı **çalışmaz**. |
| 2 | **Composio hesabı** (ücretsiz plan: ayda 100.000 araç çağrısı, kart gerekmez) | composio.dev → Sign up. Bağlantı sırasında da açabilirsin. |
| 3 | **Claude hesabı** | claude.ai veya Claude masaüstü uygulaması. Free planda en fazla 1 özel bağlayıcı eklenebilir. Team/Enterprise'da bağlayıcıyı önce yönetici açmalı. |

## 1. claude.ai tarafı: Composio bağlayıcısını ekle (3 dk)

1. Claude'da sol menüden **Customize → Connectors** aç.
2. Üstteki **+** düğmesi → **Add custom connector**.
3. **Name** alanına `Composio` yaz.
4. **MCP server URL** alanına şunu yapıştır ve **Continue** de:
   ```
   https://connect.composio.dev/mcp
   ```
5. **Connect** düğmesine bas; açılan pencerede Composio'ya giriş yap ve izni onayla.

## 2. Instagram'ı Composio'ya bağla (2 dk)

**Yol A — sohbetten:** Yeni bir sohbet aç ve yaz:
```
Instagram hesabımı Composio ile bağla.
```
Claude'un verdiği bağlantıdan Instagram'a giriş yap ve izin ver. Bağlantının süresi dolarsa Claude'dan tekrar denemesini iste.

**Yol B — Composio panelinden:** composio.dev → **Apps** → arama kutusuna `instagram` → Instagram sayfasında **Connect New** → Instagram'a yönlendirilirsin, giriş yap ve izin ver → "Connected successfully" görünce pencere kendi kapanır.

Claude Composio'yu kullanmıyorsa: sohbet kutusunda **+ → Connectors → Manage connectors** bölümünden Composio'yu aç ve tekrar sor.

## 3. Onay kuralını yaz (ilk mesaj, her yeni sohbette)

Composio **sadece okumaz**: paylaşım yapabilir ve DM gönderebilir. Bu yüzden her yeni sohbette ilk mesajın şu olsun:
```
Paylaşım ve DM'den önce her zaman onayımı iste.
```
Bu depodaki `claude-config/CLAUDE.md` aynı kuralı kalıcı olarak Claude Code'a da uygular (bkz. "Instagram ve Sosyal Medya Çalışma Kuralları").

## 4. Claude Code tarafı (kendi bilgisayarında)

claude.ai'deki bağlayıcı Claude Code'a kendiliğinden gelmez. İki seçenek:

**Seçenek 1 — bu depo (önerilen):** Bu depoyu klonladığında `.mcp.json` içinde `composio` girişi zaten var. Claude Code'u depo klasöründe başlat, `/mcp` yaz, listeden **composio** seç, **Authenticate** de ve açılan tarayıcıda Composio'ya giriş yap.

**Seçenek 2 — global kurulum:**
```bash
claude mcp add --transport http composio https://connect.composio.dev/mcp
claude            # başlat
/mcp              # composio → Authenticate
claude mcp list   # composio listede görünmeli
```
Instagram henüz bağlı değilse Claude Code'a yaz: «Instagram hesabımı Composio ile bağla.»

## 4b. Composio'ya giriş: "GitHub ile devam et" hata veriyorsa

Composio'nun giriş ekranı (`connect.composio.dev/login` → `login.composio.dev`, WorkOS AuthKit altyapısı) GitHub, Google ve e-posta ile giriş sunar. **GitHub yalnızca Composio hesabının kimliğidir; Instagram bağlantısıyla ilgisi yoktur.** GitHub butonu hata veriyorsa en hızlı çözüm aynı ekranda **e-posta** (tek kullanımlık kod / sihirli bağlantı) veya **Google** ile giriş yapmaktır; sonraki adımlar birebir aynıdır.

GitHub ile ısrar edeceksen sırayla kontrol et:

| # | Kontrol | Nasıl |
|---|---|---|
| 1 | GitHub e-postan doğrulanmış mı? | github.com → Settings → Emails: birincil adres "Verified" olmalı. Doğrulanmamış e-posta sosyal girişte en sık hata nedenidir. |
| 2 | "Keep my email addresses private" açık mı? | Aynı sayfada bu seçenek açıksa GitHub, uygulamaya `noreply` adresi verir; bazı sağlayıcılar bunu reddeder. Geçici olarak kapat, giriş yap, sonra tekrar aç. |
| 3 | Aynı e-postayla daha önce Google/e-posta ile Composio hesabı açtın mı? | "Account already exists" türü hata: o yöntemle gir (hesap zaten var). |
| 4 | Açılır pencere / üçüncü taraf çerez engeli | Tarayıcının açılır pencere engelleyicisini bu site için kapat; gizli pencerede veya başka tarayıcıda dene. Brave/Safari'de "cross-site tracking" engeli OAuth dönüşünü kesebilir. |
| 5 | GitHub tarafında yarım kalmış yetki | github.com → Settings → Applications → Authorized OAuth Apps: "Composio"/"WorkOS" varsa Revoke, sonra tekrar dene. |
| 6 | Claude Code'da `/mcp` → Authenticate döngüde kalıyorsa | Tarayıcı, Claude Code'un çalıştığı makinede açılmalı (geri dönüş `localhost` adresine yapılır). Uzak/SSH ortamında çalışmaz. Bilinen bir Claude Code hatası (anthropics/claude-code #78612): tarayıcı "başarılı" dese de "needs authentication" kalabilir; `claude mcp remove composio` → `claude mcp add --transport http composio https://connect.composio.dev/mcp` → yeniden `/mcp`. |
| 7 | Hâlâ hata | Hata metnini ve ekrandaki `ofid_...` referans kodunu support@composio.dev adresine gönder (Composio'nun resmi yönergesi). |

Claude.ai tarafında "Couldn't reach the MCP server" / "Authorization with the MCP server failed" görürsen: URL'nin tam olarak `https://connect.composio.dev/mcp` olduğunu kontrol et, bağlayıcıyı kaldırıp yeniden ekle.

## 5. Bulut (claude.ai/code) oturumları

Bulut oturumlarında dış ağ erişimi ortam politikasına bağlıdır. **claude-instagram** adlı kişisel ortam şu host'lara izin verir: `connect.composio.dev` (MCP), `backend.composio.dev` (API), `login.composio.dev` (OAuth giriş/token). Instagram işi yapacağın bulut oturumlarını bu ortamda başlat. Varsayılan ortamda Composio bağlantısı "proxy 403" ile reddedilir. Doğrulama (06.11.2026): OAuth metadata, JWKS ve dinamik istemci kaydı bu ortamdan başarıyla yanıt veriyor; eksik olan tek adım kullanıcının tarayıcıdan yapacağı giriş.

## 6. Doğrulama (işe yaradığını nasıl anlarsın)

Şu prompt'u çalıştır:
```
Composio ile Instagram hesabıma bak. Son 30 gönderimi erişim, kaydetme ve paylaşıma göre sırala. En iyi 5 ve en zayıf 5 gönderiyi tablo yap.
```
Tablo **senin gerçek gönderilerinle** doluyor, her gönderinin yanında erişim ve kaydetme sayısı varsa bağlantı çalışıyor demektir.

## 7. Hazır başlangıç prompt'ları

| # | Amaç | Prompt |
|---|---|---|
| 1 | Profil analizi | Yukarıdaki doğrulama prompt'u |
| 2 | Ne paylaşayım? | `Verilerime bakarak bu hafta ne paylaşmalıyım? Format, konu, kanca ve saat öner; nedenini rakamla açıkla.` |
| 3 | Rakip kancaları | `Şu 3 rakip hesabın son Reels'lerindeki ilk cümleleri karşılaştır: [hesaplar]. Hangi kanca türü daha çok izleniyor? Bana 5 yeni kanca yaz.` |
| 4 | Aylık plan | `[Ay] için 30 günlük içerik planı çıkar: tarih, format, konu, kanca, CTA. Haftada [4] paylaşım yapabilirim.` |
| 5 | DM cevapları | `Son 24 saatteki DM'leri oku. Her birine cevap taslağı yaz ve göndermeden önce bana göster; ben onaylamadan hiçbir şey gönderme.` |
| 6 | Reels kurgusu (Claude Code, Composio değil) | `[klasör] içindeki ham videoyu 30 saniyelik Reels'e çevir. Duraklamaları kes, altyazı ekle, kapak hazırla.` |

Bu depodaki skill'ler (`instagram-strategist`, `instagram-content-creator`, `instagram-analytics-reporter`, `instagram-community-manager`, `social-media-competitor-research`, `social-media-orchestrator`) bu prompt'ları daha yapılandırılmış biçimde yürütür; emin değilsen `social-media-orchestrator` ile başla.

## 8. Güvenlik ve sık hatalar

- **24 saat kuralı:** Instagram, DM cevabına yalnızca son 24 saatte sana yazan kişiler için izin verir.
- **Erişimi kapatmak:** Composio'yu bırakırsan bağlantıyı hem Composio panelinden (Apps → Instagram → Disconnect) hem Claude'dan (Manage connectors) kaldır; Instagram → Ayarlar → Uygulamalar ve web siteleri'nden de izni iptal et.
- **Kişisel hesapla denemek:** Çalışmaz; önce profesyonel hesaba geç.
- **Onay kuralını yazmamak:** Kural yoksa Claude bir DM'i ya da paylaşımı sormadan gönderebilir.
- **Planı kontrol etmeden yayınlamak:** Claude rakamlara bakar ama markanı ve kampanyalarını bilmez. Planı oku, uymayan günleri değiştir.
- **Otomasyon sınırları:** Toplu takip/takipten çıkma, beğeni botu, DM spam'i Instagram kullanım koşullarına aykırıdır ve hesap kapatma riski taşır; bu depodaki hiçbir skill/ajan bunları yapmaz.
