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
- `claude-config/skills/{cast,paint,_jutsu,design-dna}` — akademik kapsam dışı, kullanıcının ayrıca talep ettiği tasarım/creative-coding skill'leri (bkz. `AUDIT-REPORT-2026-07-21.md`):
  - `cast` / `paint` / `_jutsu/*` — [AThevon/genjutsu](https://github.com/AThevon/genjutsu) deposundan, motion design ve UI illüzyon skill'leri
  - `design-dna` — [zanwei/design-dna](https://github.com/zanwei/design-dna) deposundan, tasarım DNA'sı çıkarma/uygulama skill'i
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı: hangi bileşenlerin neden kurulduğu/kurulmadığı.
- `claude-config/AUDIT-REPORT-2026-07-21.md` — genjutsu ve design-dna depolarının güvenlik denetimi kaydı.

## Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir.

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown) oluşur. Test/derleme adımı yoktur.
- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.
