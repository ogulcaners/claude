# Bu Depo Hakkında

Bu depo, kullanıcının Claude Code akademik araştırma asistanı yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı; aynı zamanda Instagram/sosyal medya hesaplarını profesyonel olarak yönetiyor. Bkz. `claude-config/CLAUDE.md` için akademik dürüstlük kuralları, kaynak doğrulama protokolü ve **Instagram onay kapısı** kuralları.

## Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı özel skill'ler. 7 akademik skill:
  - `management-literature-reviewer` — 14 adımlı literatür taraması iş akışı
  - `organizational-theory-expert` — örgüt teorileri/örgütsel davranış danışmanlığı
  - `social-science-research-methods` — araştırma deseni/etik danışmanlığı
  - `qualitative-research-analyst` — nitel araştırma tasarımı ve analizi
  - `quantitative-research-analyst` — nicel araştırma tasarımı ve istatistik
  - `academic-writer-apa7` — APA 7 kaynak gösterme ve akademik yazım
  - `thesis-orchestrator` — tüm tez sürecini koordine eden meta-skill
- `claude-config/skills/*/SKILL.md` — 6 Instagram/sosyal medya skill'i (2026-11-06):
  - `social-media-orchestrator` — uçtan uca iş akışı ve ajan koordinasyonu (meta-skill)
  - `instagram-strategist` — hesap denetimi, konumlandırma, içerik sütunları, büyüme planı, marka rehberi
  - `instagram-content-creator` — Reels/kanca/carousel/caption/hashtag/story şablonları
  - `instagram-analytics-reporter` — metrik tanımları, rapor şablonu, karar kuralları
  - `instagram-community-manager` — DM/yorum triage, cevap taslakları, kriz protokolü
  - `social-media-competitor-research` — rakip/trend araştırma matrisi
- `claude-config/agents/*.md` — `~/.claude/agents/` ile aynı 5 alt ajan: `ig-analyst`, `ig-copywriter`, `ig-community-manager`, `ig-competitor-scout`, `ig-brand-reviewer`. Alt ajanlar yazma işlemi (paylaşım/DM) yapmaz; onay kapısı ana oturumdadır.
- `claude-config/docs/instagram-composio-kurulum.md` — Instagram'ı Composio köprüsüyle Claude'a bağlama rehberi (claude.ai, Claude Code, bulut ortamı).
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı (akademik araçlar).
- `claude-config/AUDIT-REPORT-2026-11-06-sosyal-medya.md` — 15 Instagram/sosyal medya deposunun güvenlik ve kalite denetimi kaydı.

## Senkronizasyon

Bu dosyalar `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill/ajan eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir. Yeni makineye taşıma:

```bash
cp claude-config/CLAUDE.md ~/.claude/CLAUDE.md
cp -r claude-config/skills/* ~/.claude/skills/
mkdir -p ~/.claude/agents && cp claude-config/agents/*.md ~/.claude/agents/
```

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown) oluşur. Test/derleme adımı yoktur.
- Yeni bir skill eklerken önce `claude-config/AUDIT-REPORT-*.md` dosyalarındaki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.
- Sosyal medya işlerinde çalışma çıktıları şu klasörlere yazılır (depoda tutulmaz, `.gitignore`'da): `brand/` (marka rehberi), `content/` (taslaklar), `reports/` (analiz raporları), `research/` (rakip araştırmaları), `calendar/` (içerik takvimleri).

## MCP Sunucuları

- `.mcp.json` — ElevenLabs resmî MCP sunucusu (`elevenlabs-mcp`, PyPI, yayıncı: ElevenLabs; sürüm sabitlendi: 0.12.2). `uvx` ile çalışır.
  - API anahtarı depoya **yazılmaz**; `ELEVENLABS_API_KEY` ortam değişkeninden okunur (bulut ortam ayarlarında tanımlanmalı).
  - Üretilen/okunan ses dosyaları `~/elevenlabs` dizinindedir (`ELEVENLABS_MCP_BASE_PATH`); bu dizin dışındaki dosyalar sunucu tarafından reddedilir.
  - Sürüm yükseltirken yeni sürümü önce gözden geçir, sonra `args` içindeki sürümü güncelle.
- `.mcp.json` — Composio barındırılan MCP sunucusu (`https://connect.composio.dev/mcp`, HTTP + OAuth). Instagram'ı resmi Meta Graph API üzerinden bağlar. Anahtar depoda tutulmaz; `/mcp` → composio → Authenticate ile tarayıcıdan giriş yapılır.
  - Composio **yazma** araçlarına (yayınlama, DM) sahiptir; `claude-config/CLAUDE.md`'deki onay kapısı kuralları bağlayıcıdır.
  - Bulut oturumları için `claude-instagram` adlı kişisel ortam `connect.composio.dev`, `backend.composio.dev` ve `login.composio.dev` host'larına izin verir; varsayılan ortamda bu host'lar kapalıdır.
