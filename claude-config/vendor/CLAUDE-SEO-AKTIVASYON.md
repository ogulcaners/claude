# claude-seo — Kayıt ve Yapada Dükkanı Aktivasyon Runbook'u

> Kayıt tarihi: 2026-11-09 · Durum: **KAYITLI, HENÜZ KURULU DEĞİL** (Yapada Dükkanı yeniden aktif edilince kurulacak)

## 1. Ne kaydedildi

| Alan | Değer |
|---|---|
| Kaynak | https://github.com/AgriciDaniel/claude-seo (MIT, © 2026 agricidaniel) |
| Kopyalanan commit | `6be93f45064ffbadced572b5d5c95f55fd263af0` (main, 2026-10-22) |
| Sürüm | v2.5.0 (`plugin.json`). `v2.5.0` etiketi = `219ff48`; main'den farkı **yalnızca README.md** |
| Konum | `claude-config/vendor/claude-seo/` — `.git` hariç 467 dosyanın tamamı (~8 MB) |
| İçerik | 26 skill (`skills/`), 19 alt ajan (`agents/`), 60 Python betiği (`scripts/`), 1 hook (`hooks/`), 9 opsiyonel eklenti (`extensions/`: ahrefs, banana, bing-webmaster, dataforseo, firecrawl, matomo, profound, seranking, unlighthouse), şema şablonları, testler |

Kopya donmuş bir anlık görüntüdür. Aktivasyon öncesinde upstream'de yeni sürüm varsa §4'teki farkı inceleyin.

## 2. Güvenlik denetimi (2026-11-09, salt okunur; hiçbir betik çalıştırılmadı)

- **Lisans:** MIT, ticari kullanım serbest.
- **Gizli anahtar:** Yok. Tek eşleşme `tests/test_banana_key_masking.py` içindeki sahte bir anahtar.
- **Tehlikeli örüntüler:** `eval`/`exec`/`shell=True`/`os.system`/`pickle` yok. `base64` kullanımı yalnızca görsel çözme ve Moz anahtar ayrıştırmasında.
- **Kurulum betiği (`install.sh`):** v2.5.0 etiketine sabitli. Sadece `~/.claude/skills/*` ve `~/.claude/agents/` altına kopyalama yapıyor; `settings.json`'a dokunmuyor ve `sudo` kullanmıyor.
- **Hook:** Tek bir `PostToolUse` (Edit|Write) hook'u var. Yazılan dosyada JSON-LD şemasını doğrulayan `validate-schema.py`; Node ile çalışıyor, zaman aşımı 30 sn.
- **Bağımlılıklar:** `requirements.txt` sürüm aralıklarıyla sabitli ve CVE notları içeriyor. `/seo setup` kendi izole Python ortamını ve Chromium'u kuruyor.
- **Karar:** ✅ Güvenli. Aktivasyonda kurulabilir.

### ⚠️ Çakışma

`install.sh` ana skill'i `~/.claude/skills/seo/` yoluna kopyalıyor. Bu oturumda o yolda **ECC'nin `seo` skill'i** kurulu, yani kurulum onun üzerine yazar. Ayrıca `anthropic-skills:yapada-schema`, `yapada-cro` ve benzeri Yapada skill'leri de mevcut.
→ **Plugin yolu (Seçenek A)** tercih edilmeli. Plugin, isim alanlı (`claude-seo:*`) olarak yüklenir ve ECC skill'iyle çakışmaz.

## 3. Aktivasyon adımları (Yapada Dükkanı yeniden aktif edildiğinde)

**Seçenek A — Plugin (önerilen):**
```
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup        # izole Python + Chromium
/seo doctor       # hazırlık kontrolü
```

**Seçenek B — Bu depodaki donmuş kopyadan (upstream erişilemezse):**
1. ECC `seo` skill'ini yedekle: `cp -r ~/.claude/skills/seo ~/.claude/skills/seo.ecc-backup`
2. `install.sh` GitHub'dan klonladığı için onu çalıştırmak yerine elle kopyala: `skills/seo/*` → `~/.claude/skills/seo/`, diğer `skills/*` → `~/.claude/skills/`, `agents/*.md` → `~/.claude/agents/`, `scripts`/`hooks`/`schema`/`data` → `~/.claude/skills/seo/`.
3. `/seo setup` ve ardından `/seo doctor` çalıştır.

**API anahtarları:** Eklentiler (DataForSEO, Ahrefs, Firecrawl vb.) ve Google API'leri (GSC, GA4, PageSpeed) anahtar istiyor. Anahtarlar **depoya veya sohbete yazılmaz**; bulut ortamının ağ gizli bilgisi (credential) olarak, sırası geldiğinde güvenli formla istenir.

## 4. Yapada Dükkanı için ilk iş planı

1. **Gerekli bilgi:** Yapada Dükkanı'nın canlı site URL'si, hedef şehir/bölge ve varsa Google Search Console ile Google Business Profile erişimi. İlgili depolar: `ogulcaners/yapadadukkan-whatsapp-bot`, `ogulcaners/yapada-ai-context`.
2. Upstream'i kontrol et: `git ls-remote --tags https://github.com/AgriciDaniel/claude-seo`. v2.5.0'dan yeni bir sürüm varsa `install.sh`, `hooks/` ve `requirements.txt` farkını yeniden denetle.
3. Kurulumu Seçenek A ile yap.
4. Taban çizgisi: `/seo audit <url>` ve `/seo drift baseline <url>` (ileride `drift compare` ile karşılaştırma yapmak için).
5. Yerel dükkan odağı: `/seo local <url>`, `/seo maps`, `/seo schema <url>` (LocalBusiness/Store), `/seo ecommerce <url>` (ürün şeması).
6. AI arama: `/seo geo <url>` ve `/seo agentic audit <url>`.
7. Sonuçları önceliklendirilmiş bir eylem planına dönüştür. Mevcut `yapada-schema`, `yapada-cro` ve `yapada-directory-submissions` skill'leriyle uygulamaya geç.

## 5. Tam komut listesi (`skills/seo/SKILL.md`)

`audit`, `page`, `sitemap`, `schema`, `images`, `technical`, `content`, `content-brief`, `geo`, `agentic`, `plan`, `programmatic`, `competitor-pages`, `local`, `maps`, `hreflang`, `google`, `backlinks`, `cluster`, `sxo`, `drift baseline|compare|history`, `ecommerce`, `matomo`*, `firecrawl`*, `dataforseo`*, `image-gen`*, `flow`, `setup`, `doctor` (* = eklenti gerektirir)
