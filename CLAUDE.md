# Bu Depo Hakkında

Bu depo, kullanıcının Claude Code yapılandırmasının **sürüm kontrollü yedeğidir**. Asıl çalışan yapılandırma bu ortamda `~/.claude/` altında yaşar (skills, global CLAUDE.md); bu depo o yapılandırmanın `claude-config/` altındaki bir kopyasını tutar ki değişiklikler izlenebilsin ve gerekirse başka bir makineye taşınabilsin.

Kullanıcı profili: İşletme Anabilim Dalı — **Yönetim ve Organizasyon** yüksek lisans programına başvurmuş bir akademik araştırmacı; aynı zamanda Yapada Kırtasiye (Margi AVM, Edirne) mağaza sahibi. Bkz. `claude-config/CLAUDE.md` için tam akademik dürüstlük kuralları ve kaynak doğrulama protokolü.

Bu depo ayrıca Yapada Kırtasiye'deki **ADA mağaza robotu** (Mini Ada 3, Akınrobotics) için Claude tabanlı mühendislik mimarisini de barındırır — bkz. `ada-robot/` klasörü.

## Dizin Yapısı

- `claude-config/CLAUDE.md` — `~/.claude/CLAUDE.md` ile aynı içerik (global akademik kurallar, kaynak doğrulama protokolü).
- `claude-config/skills/*/SKILL.md` — `~/.claude/skills/` ile aynı özel skill'ler:
  - Akademik/tez skill'leri (7 adet): `management-literature-reviewer`, `organizational-theory-expert`, `social-science-research-methods`, `qualitative-research-analyst`, `quantitative-research-analyst`, `academic-writer-apa7`, `thesis-orchestrator`
  - ADA robot skill'leri (9 adet, bkz. aşağıdaki bölüm): `ada-core`, `ada-retail-sales`, `ada-navigation`, `ada-face-recognition`, `ada-voice-dialogue`, `ada-memory-rag`, `ada-safety`, `ada-testing-evals`, `ada-observability`
  - Harici robotics mühendislik skill'leri (9 adet, `arpitg1304/robotics-agent-skills`'den vendored, Apache-2.0): `ros2`, `robotics-software-principles`, `robotics-design-patterns`, `robot-perception`, `robotics-testing`, `docker-ros2-development`, `ros2-web-integration`, `robot-bringup`, `robotics-security` — kaynak, lisans ve vendored commit için `ada-robot/vendor/robotics-agent-skills/`'e bak.
- `claude-config/AUDIT-REPORT-2026-07-17.md` — 18 harici GitHub deposunun güvenlik denetimi kaydı: hangi bileşenlerin neden kurulduğu/kurulmadığı.
- `ada-robot/` — ADA mağaza robotu için Claude-hazır mimari paketi (bkz. `ada-robot/README_START_HERE.md`):
  - `ada-robot/CLAUDE.md` — ADA üzerinde çalışırken geçerli olan mühendislik anayasası (bu kök CLAUDE.md'nin genel kurallarına ek olarak).
  - `ada-robot/MASTER_PROMPT_FOR_CLAUDE.md` — Akınrobotics yapay zeka ekibiyle yürütülecek mimari çalışma için Claude'a verilecek görevlendirme promptu.
  - `ada-robot/RESEARCH_REPORT.md`, `ada-robot/docs/GITHUB_REPOSITORIES.md` — hangi harici GitHub depolarının (arpitg1304/robotics-agent-skills, automatika-robotics/emos, vb.) benimseneceği/referans alınacağı/reddedileceği kararları.
  - `ada-robot/architecture/` — hedef sistem mimarisi, prompt mimarisi, durum makinesi, navigasyon, ses/görü, güvenlik, gözlemlenebilirlik, dağıtım yol haritası.
  - `ada-robot/prompts/` — runtime sistem promptu, geliştirici devir promptu, olay analizi promptu.
  - `ada-robot/configs/`, `ada-robot/schemas/`, `ada-robot/behavior_trees/`, `ada-robot/evals/` — mağaza haritası, tool/robot state şemaları, davranış ağaçları, regresyon/red-team test senaryoları.
  - `ada-robot/docs/AKINROBOTICS_QUESTIONS.md` — Akınrobotics yapay zeka/robotik ekibine sorulması gereken açık sorular listesi (navigasyon API'si, tool calling formatı, yüz tanıma güven eşikleri, güvenlik/e-stop mimarisi vb.). Yeni bir sistem kurulmadan önce bu sorular yanıtlanmalı.
  - `ada-robot/.claude/skills/` — pakette teslim edilen 9 ADA skill'i **artı** `arpitg1304/robotics-agent-skills`'den kurulan 9 harici robotics skill'i (toplam 18), bağımsız bir ADA/robotics reposuna doğrudan kopyalanabilir taşınabilir kopya olarak.
  - `ada-robot/vendor/robotics-agent-skills/` — vendored harici skill paketinin kaynak notu: `LICENSE` (Apache-2.0), üst `README.md` ve `VENDORED_COMMIT.txt` (klonlandığı commit hash'i, güncelleme/telif takibi için).

## Senkronizasyon

`claude-config/` dosyaları `~/.claude/` altındaki canlı yapılandırmadan **manuel olarak kopyalanmıştır** (otomatik senkronizasyon yoktur). `~/.claude/` altında yeni bir skill eklenir veya CLAUDE.md güncellenirse, bu depodaki `claude-config/` kopyasının da güncellenmesi ve commit edilmesi gerekir. `ada-robot/` bu senkronizasyon kapsamının dışındadır — o bir Claude config yedeği değil, ayrı bir mühendislik projesinin (ADA robotu) versiyonlanan spesifikasyon paketidir.

## Bu Depoda Çalışırken

- Bu depo bir uygulama/kod projesi değildir; içeriği Claude Code yapılandırma dosyalarından (Markdown/YAML/JSON/XML) oluşur. Test/derleme adımı yoktur.
- Yeni bir akademik skill eklerken önce `claude-config/AUDIT-REPORT-2026-07-17.md`'deki karar kayıtlarını kontrol et — daha önce değerlendirilip reddedilmiş bir bileşeni tekrar önermeden önce gerekçeyi gözden geçir.
- ADA robotu üzerinde çalışırken önce `ada-robot/CLAUDE.md`'deki mühendislik kurallarını ve `ada-robot/docs/GITHUB_REPOSITORIES.md`'deki harici depo kararlarını gözden geçir — LLM'nin doğrudan motor/navigasyon komutu üretmesi yasaktır; tüm fiziksel eylemler allowlist'li, şemalı tool call'lar üzerinden ve deterministik bir yürütme katmanından geçmelidir.
