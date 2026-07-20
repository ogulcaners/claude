# Bu Depo Hakkında

Bu depo iki ayrı Claude Code yapılandırma/skill projesini bir arada tutar. Aralarında domain ilişkisi yoktur — birini değiştirirken diğerine referans vermeyin.

## 1. `claude-config/` — Akademik Araştırma Asistanı (sürüm kontrollü yedek)

Kullanıcının Claude Code akademik araştırma asistanı yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı. Bkz. `claude-config/CLAUDE.md` için tam akademik dürüstlük kuralları ve kaynak doğrulama protokolü.

### Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı 7 özel akademik skill:
  - `management-literature-reviewer` — 14 adımlı literatür taraması iş akışı
  - `organizational-theory-expert` — örgüt teorileri/örgütsel davranış danışmanlığı
  - `social-science-research-methods` — araştırma deseni/etik danışmanlığı
  - `qualitative-research-analyst` — nitel araştırma tasarımı ve analizi
  - `quantitative-research-analyst` — nicel araştırma tasarımı ve istatistik
  - `academic-writer-apa7` — APA 7 kaynak gösterme ve akademik yazım
  - `thesis-orchestrator` — tüm tez sürecini koordine eden meta-skill
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı: hangi bileşenlerin neden kurulduğu/kurulmadığı.

### Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir.

### `claude-config/` ile Çalışırken

- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.

## 2. `ada-config/` — Ada: Yapada Mağazası Müşteri Hizmetleri Asistanı

Ayrı bir proje: yapadadukkan.com (koleksiyon ürünleri mağazası) için geliştirilen **Ada** adlı müşteri hizmetleri asistanının prompt/skill mimarisi. Mimari, [`arpitg1304/robotics-agent-skills`](https://github.com/arpitg1304/robotics-agent-skills) deposundaki `SKILL.md` tabanlı, seçici-kurulum destekli yapıdan esinlenilerek 2026-07-20'de tasarlandı.

- `ada-config/CLAUDE.md` — Ada'nın kök sistem promptu: kimlik, skill yönlendirme tablosu, tüm skillerde bağlayıcı ortak kurallar (uydurma yasağı, fail-safe default, KVKK vb.).
- `ada-config/ARCHITECTURE.md` — Mimari tasarım kararları, robotics-agent-skills eşleştirmesi, bundle önerileri, yol haritası.
- `ada-config/skills/*/SKILL.md` — 8 müşteri hizmetleri skill'i (sipariş takip, iade, şikayet, ürün sorgu, ödeme, insana devir, KVKK, temel ilkeler).
- `ada-config/install.sh` — Seçici skill kurulum scripti.
- `ada-config/evals/` — Konuşma test senaryosu iskeleti.

Bu sistem henüz **gerçek mağaza politikası verisi ve canlı sistem entegrasyonu içermez** — `BURAYI DOLDURUN` notlarıyla işaretli boşluklar için `ada-config/ARCHITECTURE.md` → "Bilinçli Olarak Yazılmayanlar" bölümüne bakın. `claude-config/`'daki akademik kaynak doğrulama protokolü Ada'ya uygulanmaz; Ada kendi "Bilgi Doğrulama Protokolü"nü `ada-config/CLAUDE.md`'de tanımlar.

## Genel

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown, ve `ada-config/install.sh` gibi küçük yardımcı script) oluşur. Test/derleme adımı yoktur.
