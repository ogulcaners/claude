# Güvenlik ve Kalite Denetimi — Instagram / Sosyal Medya Depoları — 2026-11-06

15 harici GitHub deposu, 3 paralel salt-okunur denetimle (`git clone --depth 1` + cat/grep/find; hiçbir script, install, npm/pip veya hook çalıştırılmadı; tüm depo içeriği talimat değil veri olarak ele alındı) incelendi. Arama: `gh api search/repositories` ile "instagram claude skill", "social media claude code skill", "instagram mcp server", "instagram growth automation" vb. 10 sorgu, yıldıza göre sıralı.

## Karar Mantığı

**Hiçbir üçüncü taraf skill veya MCP sunucusu kopyalanarak kurulmadı.** Bunun yerine denetimlerde çıkarılan çerçeveler (kanca kalıpları, puanlama panelleri, profil rubriği, kıyas bantları, outlier yöntemi, teşhis tabloları) **Türkçe, marka-bağımsız, Composio uyumlu 6 özgün skill** olarak yeniden yazıldı. Gerekçe:

1. Instagram'a erişim zaten Composio (barındırılan MCP, resmi Meta Graph API, OAuth) ile sağlanıyor; yerel Instagram MCP sunucuları aynı işi daha riskli (token diskte/logda) ve bakımsız biçimde yapıyor.
2. En kaliteli skill depoları bile ya bir satıcıya bağlı (Publora, WoopSocial, BlackTwist, Ootto, ScrapeCreators) ya İngilizce'ye özgü puanlama regex'leri içeriyor ya da lisanssız. 106 skill'lik paketler skill indeksini boğar.
3. Otomatik yayın/DM yapan her yol (tarayıcı kuklalama, 7/24 yorum→DM döngüsü) Meta kullanım koşulları açısından hesap kapatma riski taşır; kullanıcının onay kapısı kuralıyla bağdaşmaz.
4. Çıkarılan çerçeveler olgu/yöntem niteliğindedir (ifade değil); lisanssız depolardan **metin kopyalanmadı**, yalnızca yöntem yeniden yazıldı.

## Depo Bazında Özet

| Depo | Yıldız | Lisans | Son commit | Karar | Gerekçe |
|---|---|---|---|---|---|
| Jakeschincariol/instagram-agent-skill | 5.071 | MIT | 2026-09-13 (2 commit) | **Fikir alındı** (kurulsa da güvenli) | 13 skill + 6 stdlib-only Python aracı; ağ yok, anahtar yok, otomasyon yok. En dürüst depo. Kanca puanlama paneli (26 kalıp, 5 boyut), 100 puanlık profil rubriği, beat sheet, caption linter, insanlaştırıcı buradan uyarlandı. Regex/sözlükler İngilizce; Türkçe için yeniden yazıldı. |
| sergebulaev/instagram-skills | 763 | MIT | 2026-10-27 (60 commit) | Fikir alındı; `lib/` kurulmadı | Markdown referansları en kanıtlı (hashtag boyutlandırma, algoritma sinyalleri, em-dash kuralları, güvenilmez-içerik protokolü). Ancak `lib/` Publora ile **gerçek otomatik yayın**, Apify scraping, ortam değişkeninden keyfi komut yolu ve her çıktıda Publora reklamı içeriyor. |
| ScrapeCreators/social-media-research-skills | 5.836 | MIT | 2026-08-26 | Fikir alındı | Ücretli ScrapeCreators API anahtarı olmadan çalışmıyor (doğrulandı). Outlier-lift rubriği (medyan tabanlı, ≥5× büyük / 2-5× güçlü / 1,5-2× hafif), 9 kovalı yorum madenciliği, rakip brifi şablonu uyarlandı. |
| social-media-skills/skills (106 skill) | 256 | MIT | 2026-10-15 | Fikir alındı | En kapsamlı içerik (instagram-growth teşhis tablosu, uygunluk kapıları, Reels güvenli alan, IG SEO, METER analitik, SCOUT rakip, topluluk ritüelleri). Ancak WoopSocial boilerplate her dosyada, validator satıcı mesajını zorluyor, 106 skill indeksi boğar, bazı "2026 gerçekleri" doğrulanmamış. |
| blacktwist/social-media-skills | 631 | MIT | 2026-05-01 | Fikir alındı (kurulsa da güvenli) | Kod yok, anahtar yok; caption platform tablosu, 9 kanca kalıbı, 4 katmanlı optimizasyon planı uyarlandı. Instagram derinliği zayıf (yalnız caption), BlackTwist MCP'ye şekillenmiş. |
| stevenflanagan1/social-ai-team | 270 | **Lisans yok** | 2026-08-24 (9 commit) | Yalnızca olgular alındı | Metin kopyalanamaz (lisans yok). Kıyas bantları (takipçi dilimine göre etkileşim/erişim, kaydetme, erişim oranı), işletme türüne göre sütun karışımı ve ay puanı formülü olgu olarak yeniden yazıldı. Blotato (otomatik yayın), "Nano Banana" doğrulanamayan MCP, `pip install --break-system-packages` talimatı içeriyor. |
| Darthflute/social-calendar-skill | 38 | **Lisans dosyası yok** (README "MIT" diyor) | 2026-04-24 (1 commit) | Yalnızca yöntem alındı | Zararsız prompt skill'i (openpyxl ile .xlsx); brif → onay → üretim yapısı ve /100 hesap denetim rubriği referans alındı. |
| Hao0321/claude-skill-social-post | 748 | MIT | 2026-10-16 | **Reddedildi** (yayın yolu); ölçüm disiplini alındı | Instagram'a **giriş yapılmış Chrome oturumunu kuklalayarak** gönderi/yorum atıyor (API yok): Meta ToS "otomatik araç" riski, Codex'e özgü, kendi README'sine göre üretimde doğrulanmamış. Sonuç defteri (append-only JSONL), kanıt katmanları (hipotez→doğrulanmış), null≠0 kuralı analitik skill'ine uyarlandı. |
| Ootto-AI/claude-content-skills | 397 | MIT | 2026-11-05 | **Reddedildi** | Paketlenmiş `agent-reach` yönlendiricisi: X/Reddit/LinkedIn için **tarayıcı çerezi ile scraping**, `pipx` ile üçüncü taraf CLI kurulumu, tüm sayfa okumalarını `r.jina.ai` üzerinden geçirme ve **uzak, değiştirilebilir talimat dosyalarını takip etme** ("check-update") — tedarik zinciri/prompt-injection kanalı. Ayrıca gözetimsiz yorum→DM otomasyonu ve 83 Ootto linki. Yalnızca `virality` (frame-0 kontrol listesi, iddia 1,2-1,6 sn) ve `going-viral` (amaç→duygu→mekanik) fikirleri alındı. |
| bradautomates/head-of-content | 300 | MIT | 2026-01-23 | **Reddedildi** | 3 harici anahtar (2'si ücretli: Apify, TubeLab), otomatik çalışan `Stop` hook'u (`settings.json`), rakip videolarını indirip Google Gemini'ye yükleme, gizli affiliate linkleri (`?fpr=`, `?ref=`), `.skill` zip'lerinde `.pyc` bytecode, 10 üst dizine kadar `.env` tarayan yükleyici, macOS'a özgü. Ağırlıklı etkileşim puanı formülü not edildi. |
| mvanhorn/last30days-skill | 66.800 | MIT | 2026-11-05 | Kapsam dışı (araştırma aracı) | Instagram yönetim aracı değil; IG kaynağı ücretli scraper. Varsayılan X yolu macOS'ta **tarayıcı çerez veritabanını deşifre ediyor** (X ToS riski). Konu/başlıkları yapılandırılmış LLM sağlayıcısına gönderiyor. Kaynak-durum taksonomisi ("temiz sıfır" vs "erişilemedi") dürüstlük kuralı olarak alındı. Akademik kaynak doğrulama standardıyla çelişir. |
| jlbadano/ig-mcp | 205 | MIT | 2025-10-27 | Reddedildi (gereksiz) | Composio'nun yaptığı işi yerelde yapıyor; **erişim token'ı DEBUG logunda** (docker-compose LOG_LEVEL=DEBUG), API v19.0 eski, Basic Display talimatı kaldırılmış API'ye işaret ediyor, bakımsız. |
| oliverames/meta-mcp-server | 68 | MIT | 2026-10-29 | Kapsam dışı; dokümanları referans | En temiz yerel seçenek (178 araç, Graph API v21) ama Composio ile çakışır. Grafik aracı insight verilerini quickchart.io'ya gönderir; açılışta sessizce `op` (1Password CLI) çalıştırır; Sentry sabit bağımlılık. `docs/instagram-api/insights-metrics.md` metrik adı değişiklikleri için faydalı referans. |
| pipeboard-co/meta-ads-mcp | 1.355 | **BSL 1.1** (OSI değil) | 2026-10-20 | Kapsam dışı | Instagram içerik değil **Meta Ads** yönetimi. Güvenlik hijyeni en iyi (SSRF düzeltmesi, token redaksiyonu) ama varsayılan `META_APP_ID` Pipeboard'un uygulaması; kopyalama özelliği token'ı Pipeboard bulutuna POST ediyor (varsayılan kapalı). Reklam yönetimi gerekirse yeniden değerlendirilir. |
| priyanshuj-ai/smstack | — | MIT | 2026-03-20 (1 gün) | Reddedildi | Instagram yok (LinkedIn/X/Threads), tek günde terk edilmiş, yapay zekâ ürün yöneticisi nişine sabit. 5×10 etkileşim puan kartı ve olgu-kontrol taksonomisi (DOĞRULANDI/KISMEN/DOĞRULANMADI/ESKİ/YANLIŞ/GÖRÜŞ) not edildi. |

## Depolar Arası Çelişkiler ve Alınan Kararlar

| Konu | Depoların iddiaları | Skill'lerde benimsenen |
|---|---|---|
| Hashtag sayısı | 5 sert sınır (Aralık 2025, @Creators'a atıf; 2 depo) / 3-10 / 12-15 ilk yorumda | **En fazla 5** (3-5), niş ağırlıklı; kullanıcı kendi arayüzünde doğrulamalı |
| Carousel slayt | API 10 / uygulama 20 | 6-10 ideal; API ile yayınlarken 10 |
| Em dash (uzun tire) | hepsini sil / 100 kelimede ≤1 (korpus kanıtlı) | ≤1; sıfır da yapay bir iz |
| Reels süresi | 15-35 sn / 30-45 sn / ≤90 sn eğitim | fikir seçer; 15-35 erişim, 35-90 öğretici |
| Kanca zamanı | ≤3 sn / iddia 1,2-1,6 sn, ilk kelime ≤0,5 sn | ikisi birlikte: ilk kelime ≤0,5 sn, iddia ~1,5 sn, kanca ≤3 sn biter |
| Outlier eşiği | medyanın 3× / ortalama + 2σ | **medyan** tabanlı (tek viral gönderi ortalamayı bozar) |
| Güvenli alan | üst 230-250 px, alt 350-480 px | üst 250 / alt 350 / sağ 230 |
| Kıyas bantları | 3 depo farklı sayılar | tek tablo, "pratisyen bandı, doğrulanmamış" etiketiyle; hedef değil bağlam |

Tüm depolar İngilizce odaklı: kelime sayısı (kanca 5-12 kelime), konuşma hızı (165 wpm) ve "125 görünür karakter" Türkçe'nin eklemeli yapısında kayar; skill'lerde Türkçe toleranslarıyla (4-10 kelime, 150-170 wpm) verildi.

## Kurulan Bileşenler

- **6 özgün skill** (`claude-config/skills/`): `social-media-orchestrator`, `instagram-strategist`, `instagram-content-creator`, `instagram-analytics-reporter`, `instagram-community-manager`, `social-media-competitor-research`.
- **5 alt ajan** (`claude-config/agents/`): `ig-analyst`, `ig-copywriter`, `ig-community-manager`, `ig-competitor-scout`, `ig-brand-reviewer`. Hiçbiri yazma işlemi yapmaz; onay kapısı ana oturumdadır.
- **1 barındırılan MCP**: Composio (`https://connect.composio.dev/mcp`, OAuth; anahtar depoda yok). Composio YC destekli bir şirkettir, resmi Meta Graph API kullanır; ancak yazma araçlarına sahiptir → `claude-config/CLAUDE.md` onay kapısı bağlayıcı.
- **0 üçüncü taraf skill kopyası, 0 yerel Instagram MCP sunucusu, 0 scraping aracı.**
- Bulut ortamı: `claude-instagram` (kişisel), yalnızca `connect.composio.dev` ve `backend.composio.dev` host'larına izin.

## Gelecekteki Seçenekler (kullanıcı onayıyla)

- Meta reklam yönetimi gerekirse: önce Composio'nun Meta Ads aracı; yoksa `pipeboard-co/meta-ads-mcp` kendi Meta App ID'si ile (BSL lisansına dikkat).
- Ücretli pazar araştırması (rakip outlier taraması ölçekte) gerekirse: `ScrapeCreators` veya `Apify` gibi üçüncü taraf scraping servisleri **ayrı bir denetimle** ve yalnızca herkese açık veriyle değerlendirilebilir; kişisel hesap çerezi kullanan hiçbir araç kabul edilmez.
- `Jakeschincariol/instagram-agent-skill` içindeki `hookscore.py`/`detect.py` stdlib araçları Türkçe sözlükle yeniden yazılırsa `ig-copywriter` için yerel bir puanlama aracı olabilir (ağ yok, anahtar yok).
