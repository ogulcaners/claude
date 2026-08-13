# Bu Depo Hakkında

Bu depo, kullanıcının Claude Code akademik araştırma asistanı yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı. Bkz. `claude-config/CLAUDE.md` için tam akademik dürüstlük kuralları ve kaynak doğrulama protokolü.

## Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı 7 özel akademik skill:
  - `management-literature-reviewer` — 14 adımlı literatür taraması iş akışı
  - `organizational-theory-expert` — örgüt teorileri/örgütsel davranış danışmanlığı
  - `social-science-research-methods` — araştırma deseni/etik danışmanlığı
  - `qualitative-research-analyst` — nitel araştırma tasarımı ve analizi
  - `quantitative-research-analyst` — nicel araştırma tasarımı ve istatistik
  - `academic-writer-apa7` — APA 7 kaynak gösterme ve akademik yazım
  - `thesis-orchestrator` — tüm tez sürecini koordine eden meta-skill
  - `emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-vocabulary`, `apple-design`, `pick-ui-library`, `prototype`, `ask-sonner` — akademik kapsamın dışında, kullanıcının isteği üzerine eklenmiş tasarım/animasyon skilleri (bkz. aşağıda)
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı: hangi bileşenlerin neden kurulduğu/kurulmadığı.

## Akademik Kapsam Dışı Skiller

[emilkowalski/skills](https://github.com/emilkowalski/skills) deposunun tamamı — Emil Kowalski'nin (Vercel/Linear, Sonner/Vaul yazarı) UI animasyon/geçiş/mikro-etkileşim tasarım felsefesini kapsayan 10 skil — 2026-08-13'te kullanıcı isteğiyle birebir kaynağından eklendi:

- `emil-design-eng` — ana felsefe/inceleme skili (taste, animasyon karar çerçevesi, spring'ler, performans, erişilebilirlik)
- `animate` — sıfırdan animasyon inşa etme
- `review-animations` — mevcut animasyon kodunu sıkı bir craft bar'a göre inceleme
- `improve-animations` — bir kod tabanının animasyon/motion kodunu denetleyip önceliklendirilmiş uygulama planları üretme (salt-okunur, kendisi uygulamaz)
- `find-animation-opportunities` — animasyon eksik olan ama olması gereken yerleri arama (salt-okunur)
- `animation-vocabulary` — belirsiz bir animasyon tarifini ("popover açılırken zıplayan şey") doğru terime çevirme
- `apple-design` — Apple'ın WWDC tasarım ilkelerinin web'e çevirisi (spring, gesture, malzeme, tipografi)
- `pick-ui-library` — frontend görevine göre küratörlü kütüphane seçimi (yalnızca açıkça çağrıldığında çalışır)
- `prototype` — bir UI parçasının birden çok farklı varyantını üretip görsel bir seçici arkasında sunma (yalnızca açıkça çağrıldığında çalışır)
- `ask-sonner` — Sonner toast kütüphanesi kurulum/kullanım/sorun giderme rehberi

Not: `prototype`, `pick-ui-library` ve `review-animations` kaynak depoda `disable-model-invocation: true` frontmatter alanı taşıyor (yalnızca açıkça çağrıldığında tetiklensin diye); bu ortamın skill doğrulayıcısı bu alanı tanımadığından paketlerken çıkarıldı — davranış amacı zaten description metninde ("Only runs when explicitly invoked...") belirtiliyor.

## Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir.

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown) oluşur. Test/derleme adımı yoktur.
- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.
