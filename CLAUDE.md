# Bu Depo Hakkında

Bu depo, kullanıcının Claude Code akademik araştırma asistanı yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı. Bkz. `claude-config/CLAUDE.md` için tam akademik dürüstlük kuralları ve kaynak doğrulama protokolü.

## Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı 7 özel akademik skill + 1 web güvenlik skill'i:
  - `management-literature-reviewer` — 14 adımlı literatür taraması iş akışı
  - `organizational-theory-expert` — örgüt teorileri/örgütsel davranış danışmanlığı
  - `social-science-research-methods` — araştırma deseni/etik danışmanlığı
  - `qualitative-research-analyst` — nitel araştırma tasarımı ve analizi
  - `quantitative-research-analyst` — nicel araştırma tasarımı ve istatistik
  - `academic-writer-apa7` — APA 7 kaynak gösterme ve akademik yazım
  - `thesis-orchestrator` — tüm tez sürecini koordine eden meta-skill
  - `web-security-review` — Yapada siteleri ve yeni web işleri için güvenlik incelemesi (ECC'den uyarlandı)
- Web güvenlik denetim raporları bu depoya **konmaz** (depo public); ayrıntılı bulgular saldırı yol haritası olur.
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı: hangi bileşenlerin neden kurulduğu/kurulmadığı.

- `claude-config/environment-setup.sh` — bulut ortamının kurulum betiği: claude-config'i geri yükler ve ECC'yi (affaan-m/everything-claude-code, `d2ef268`'e sabit, hook'larla) kurar.

## Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir.

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown) oluşur. Test/derleme adımı yoktur.
- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.

## MCP Sunucuları

- `.mcp.json` — ElevenLabs resmî MCP sunucusu (`elevenlabs-mcp`, PyPI, yayıncı: ElevenLabs; sürüm sabitlendi: 0.12.2). `uvx` ile çalışır.
  - API anahtarı depoya **yazılmaz**; `ELEVENLABS_API_KEY` ortam değişkeninden okunur (bulut ortam ayarlarında tanımlanmalı).
  - Üretilen/okunan ses dosyaları `~/elevenlabs` dizinindedir (`ELEVENLABS_MCP_BASE_PATH`); bu dizin dışındaki dosyalar sunucu tarafından reddedilir.
  - Sürüm yükseltirken yeni sürümü önce gözden geçir, sonra `args` içindeki sürümü güncelle.
