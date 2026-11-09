# Bu Depo Hakkında

Bu depo, kullanıcının Claude Code akademik araştırma asistanı yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı. Bkz. `claude-config/CLAUDE.md` için tam akademik dürüstlük kuralları ve kaynak doğrulama protokolü.

## Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı skill'ler (7 özel akademik skill + 1 üçüncü taraf):
  - `management-literature-reviewer` — 14 adımlı literatür taraması iş akışı
  - `organizational-theory-expert` — örgüt teorileri/örgütsel davranış danışmanlığı
  - `social-science-research-methods` — araştırma deseni/etik danışmanlığı
  - `qualitative-research-analyst` — nitel araştırma tasarımı ve analizi
  - `quantitative-research-analyst` — nicel araştırma tasarımı ve istatistik
  - `academic-writer-apa7` — APA 7 kaynak gösterme ve akademik yazım
  - `thesis-orchestrator` — tüm tez sürecini koordine eden meta-skill
  - `find-skills` — üçüncü taraf (vercel-labs/skills, MIT); skills.sh ekosisteminde skill arama. Sonunda kurulumu onaya bağlayan yerel ek kurallar var.
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı (+ sonraki ek kararlar): hangi bileşenlerin neden kurulduğu/kurulmadığı.

## Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur).

**Geri yükleme (depo → `~/.claude/`) otomatiktir:** bulut ortamının ("claude-instagram") kurulum betiği her yeni kapsayıcıda `claude-config/CLAUDE.md` dosyasını `~/.claude/CLAUDE.md`'ye, `claude-config/skills/*` klasörlerini `~/.claude/skills/` altına kopyalar. Ters yön (canlı → depo) hâlâ manueldir; bu yüzden aşağıdaki kural geçerlidir. `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir.

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown) oluşur. Test/derleme adımı yoktur.
- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.

## MCP Sunucuları

- `.mcp.json` — ElevenLabs resmî MCP sunucusu (`elevenlabs-mcp`, PyPI, yayıncı: ElevenLabs; sürüm sabitlendi: 0.12.2). `uvx` ile çalışır.
  - API anahtarı depoya **yazılmaz**; `ELEVENLABS_API_KEY` ortam değişkeninden okunur (bulut ortam ayarlarında tanımlanmalı).
  - Üretilen/okunan ses dosyaları `~/elevenlabs` dizinindedir (`ELEVENLABS_MCP_BASE_PATH`); bu dizin dışındaki dosyalar sunucu tarafından reddedilir.
  - Sürüm yükseltirken yeni sürümü önce gözden geçir, sonra `args` içindeki sürümü güncelle.
