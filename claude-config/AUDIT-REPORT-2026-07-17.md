# Güvenlik Denetimi ve Kurulum Kararları — 2026-07-17

18 harici GitHub deposu, 6 paralel salt-okunur denetim (git clone --depth 1 + Read/Grep, hiçbir install/setup scripti çalıştırılmadı) ile incelendi. Aşağıda depo bazında bulgular ve nihai karar özetlenmiştir.

## Karar Mantığı

Hiçbir üçüncü taraf skill veya MCP sunucusu bu oturumda kurulmadı. Gerekçe:
1. Akademik kaynak doğrulama ihtiyacı (Crossref/OpenAlex/Semantic Scholar/DOI), zaten mevcut olan **WebFetch** aracıyla bu servislerin ücretsiz, anahtar gerektirmeyen REST API'lerine doğrudan istek atılarak karşılanabiliyor — üçüncü taraf kod çalıştırmaya gerek yok.
2. İncelenen akademik MCP sunucularının **her birinde** en az bir ciddi uyarı bulundu (aşağıda liste).
3. `modelcontextprotocol/servers` (filesystem/fetch/memory) gibi temiz çıkan sunucular bile Claude Code'un yerleşik araçlarıyla (Read/Write/Glob/Grep, WebFetch, auto-memory) işlevsel olarak örtüşüyor — kurulumları "gereksiz" (kullanıcının kendi talimatındaki yasak listesinde).
4. 7 özel akademik skill zaten tam olarak istenen iş akışını (14 adımlı literatür taraması, APA7, doğrulama protokolü) kapsıyor; genel amaçlı üçüncü taraf "research" skill'leri eklemek işlev çakışmasına yol açardı.

## Depo Bazında Özet

| Depo | Tür | Karar | Gerekçe |
|---|---|---|---|
| anthropics/skills | Resmi | KuruLMADI (öneri: `/plugin install` kullanıcı tarafından) | `pdf`/`docx`/`pptx`/`xlsx` özel (proprietary) lisanslı — manuel kopyalama yerine resmi plugin marketplace yolu önerilir. `doc-coauthoring` (Apache-2.0) faydalı ama özel skill'lerle örtüşüyor. |
| anthropics/claude-plugins-official | Resmi | Kurulmadı | İçerik tamamen yazılım geliştirme araçları; akademik araştırmayla ilgisi yok. |
| anthropics/knowledge-work-plugins | Resmi | Kurulmadı (isteğe bağlı not edildi) | `data/statistical-analysis`, `design/research-synthesis`, `pdf-viewer/view-pdf` temiz ama Cowork ekosistemine bağlı ve özel skill'lerle kısmen örtüşüyor. Kullanıcı isterse ileride eklenebilir. |
| VoltAgent/awesome-agent-skills | Liste (kod yok) | Kurulum gerektirmiyor | Sadece diğer depolara link veren bir dizin; kod içermiyor. |
| modelcontextprotocol/servers | Resmi | Kurulmadı | `filesystem`/`fetch`/`memory` temiz ama Claude Code'un yerleşik Read/Write/WebFetch/auto-memory ile işlevsel çakışma; gereksiz ek bağımlılık. |
| github/github-mcp-server | Resmi | Kurulmadı | Bu oturumda zaten yerleşik `github` MCP bağlantısı mevcut — birebir aynı fonksiyonlar, kurulumu gereksiz/çakışan. |
| alirezarezvani/claude-skills | Bireysel (22.7k★) | Kurulmadı | `research/*` alt kümesi temiz çıktı ama özel olarak inşa edilen 7 akademik skill ile doğrudan çakışıyor (aynı amaç, farklı uygulama) — kafa karıştırıcı/çakışan bileşen riski. |
| Imbad0202/academic-research-skills | Bireysel (38.2k★/9 issue) | **Kurulmadı — güven endişesi** | Yıldız/issue oranı istatistiksel olarak anormal; ticari olmayan lisans (CC-BY-NC-4.0); istenenin çok ötesinde kapsam (tam bir "yapay zeka ile makale yazma + hakemlik" hattı). Kod zararlı değil ama ölçek ve güvenilirlik riski yüksek. |
| openags/paper-search-mcp | Kurum (2.2k★) | **Kurulmadı — güvenlik/etik riski** | `download_scihub` aracı **varsayılan olarak açık** (`use_scihub=True`) ve bu yolda TLS sertifika doğrulaması devre dışı (`verify=False`). Sci-Hub kullanımı akademik dürüstlük/telif riski taşır — tez çalışması için kabul edilemez. |
| zongmin-yu/semantic-scholar-fastmcp-mcp-server | Bireysel (160★) | Kurulmadı | Kod temiz ama varsayılan olarak `0.0.0.0:8000` üzerinde kimliksiz bir HTTP köprüsü açıyor (yanlış yapılandırma riski). WebFetch ile aynı API doğrudan sorgulanabiliyor, ek risk almaya gerek yok. |
| hunter-heidenreich/academic-tools-mcp | Bireysel (5★, çok yeni) | Kurulmadı (izlenmeye değer) | Kod kalitesi yüksek (485 test, defusedxml, dikkatli subprocess yönetimi) ama topluluk denetimi neredeyse yok (~3.5 aylık, 5 yıldız). WebFetch alternatifi yeterli. |
| tfscharff/doi-mcp | Bireysel (15★) | Kurulmadı | `dist/` klasöründe kaynak koduyla eşleşmeyen, doğrulanamayan derlenmiş dosyalar var (tedarik zinciri riski); LICENSE dosyası eksik; CI yok. |
| zotero/zotero | Uygulama kaynağı | Kurulum kapsamı dışı | Bu, Zotero masaüstü uygulamasının kaynak kodudur — bir skill/MCP değildir. Kullanıcı Zotero'yu kendi bilgisayarına ayrıca kurmalı. |
| 54yyyu/zotero-mcp | Bireysel (aktif, olgun) | **Kurulmadı burada — kullanıcının kendi bilgisayarı için önerilir** | Denetimde temiz çıktı (MIT, aktif bakım, şeffaf izinler) ancak çalışması için kullanıcının kendi bilgisayarında **yerel olarak çalışan bir Zotero uygulaması** gerektiriyor — bu uzak/geçici oturumda mevcut değil. Kullanıcı kendi makinesinde Zotero kullanıyorsa gelecekte kurulması önerilir. |
| benchoi93/refcheck | Bireysel (erken aşama) | Kurulmadı | Kod temiz, anahtar gerektirmiyor, ama 9 commit/v0.1.0/CI yok — olgunlaşmamış. WebFetch ile Crossref/Semantic Scholar doğrudan sorgulanabiliyor. |
| massimoaria/bibliometrix | R paketi | Kapsam dışı | Bir Claude skill/MCP değil; R/RStudio ortamı gerektiren ayrı bir istatistik paketi. Kullanıcı bibliometrik analiz isterse Claude R kodu yazarak destek olabilir. |
| citation-style-language/styles | Referans deposu | Kurulum yok, **referans olarak not edildi** | `apa.csl` ve `apa-tr.csl` güncel/resmi APA 7 stil dosyaları — Zotero/Pandoc kullanılırsa referans olarak `academic-writer-apa7` ve `~/.claude/CLAUDE.md`'de belirtildi. |
| quarto-dev/quarto-cli | CLI araç | Kapsam dışı | Tam sistem kurulumu gerektiren ayrı bir yayınlama sistemi; kullanıcı Markdown/Quarto tabanlı yazıma geçmek istemedikçe gereksiz. |

## Kurulan Bileşenler

- **7 özel akademik skill** (`~/.claude/skills/`): management-literature-reviewer, organizational-theory-expert, social-science-research-methods, qualitative-research-analyst, quantitative-research-analyst, academic-writer-apa7, thesis-orchestrator.
- **0 üçüncü taraf MCP sunucusu.**
- **Kaynak doğrulama protokolü**: WebFetch ile Crossref/OpenAlex/Semantic Scholar/DOI.org doğrudan sorgulanıyor (`~/.claude/CLAUDE.md`).

## Kullanıcı İçin Gelecekteki Seçenekler (kendi onayıyla)

- Kendi bilgisayarında Zotero kullanıyorsa: `54yyyu/zotero-mcp` kurulabilir (Zotero masaüstü + "Allow other applications..." ayarı gerekir).
- Word/PDF üretimi için Anthropic'in resmi `docx`/`pdf`/`doc-coauthoring` skill'leri `/plugin marketplace add anthropics/skills` ve `/plugin install document-skills@anthropic-agent-skills` ile kurulabilir.

## Ek Değerlendirme — 2026-08-17: open-free-llm-api/awesome-freellm-apis

Kullanıcı bu depoyu paylaştı. Salt-okunur inceleme yapıldı (`git clone --depth 1`, README + `code-examples/` okundu, hiçbir script çalıştırılmadı).

**Ne olduğu:** Bu bir Claude skill'i veya MCP sunucusu değil — 31 sağlayıcıdan 442+ ücretsiz LLM API'sini listeleyen, çalıştırılabilir kod içermeyen bir "awesome list" / dizin deposu (`README.md` + 4 dil çevirisi + `code-examples/*.md`). Ticari bir sitenin (freellm.net, günlük otomatik güncelleniyor) statik aynası niteliğinde. Yukarıdaki tabloda `VoltAgent/awesome-agent-skills` için işaretlenenle aynı kategori: "Liste (kod yok) | Kurulum gerektirmiyor".

**Karar: Hiçbir şey kurulmadı/taşınmadı.** Gerekçe:
1. **Kategori uyuşmazlığı** — akademik iş akışıyla (tez/literatür/APA7/kaynak doğrulama) hiçbir ilgisi yok; bu bir ticari LLM API sağlayıcı karşılaştırma dizini.
2. **Çalıştırılabilir kod içermiyor** — `code-examples/` altındaki dosyalar sadece kopyala-yapıştır ortam değişkeni/kod parçacıkları; script, `postinstall`, veya MCP tanımı yok.
3. **Önemli uyarı — kullanıcıya önerilmemesi gereken bir yapılandırma içeriyor:** `code-examples/claude-code.md`, Claude Code'un `ANTHROPIC_BASE_URL` ve `ANTHROPIC_AUTH_TOKEN` ortam değişkenlerini Anthropic dışındaki üçüncü taraf sağlayıcılara (Groq, NVIDIA NIM, OpenRouter, Cloudflare Workers AI, SiliconFlow vb.) yönlendirmeyi ve bunu kalıcı olarak `~/.zshrc`/`~/.bashrc`'a eklemeyi öneriyor. Bu, Claude Code'a girilen TÜM istekleri — kullanıcının tez taslakları, kaynak metinleri, akademik notları dahil — Anthropic'in kendi altyapısı yerine doğrulanamayan üçüncü taraf sağlayıcılara yönlendirmek anlamına gelir. Depo sadece dokümantasyon olduğu için "kurulmadı" sayılıyor, ama bu spesifik yapılandırma **veri gizliliği/güven modeli riski nedeniyle kullanıcıya önerilmeyecek**.
4. **Kaynak güvenilirliği sınırlı doğrulanabildi** — "open-free-llm-api" organizasyonu az bilinen bir kaynak; depo ticari bir siteye (freellm.net) trafik yönlendiriyor. Kötü niyetli bir şey tespit edilmedi (MIT lisans, script yok) ama bağımsız doğrulama sınırlı.

**Kullanıcı için not:** Akademik asistan dışındaki kişisel/geliştirme projeleri için ücretsiz LLM API'leri karşılaştırmak isterse bu depo/site bir başlangıç noktası olabilir; ancak Claude Code'un `ANTHROPIC_BASE_URL`/`ANTHROPIC_AUTH_TOKEN` değerlerini üçüncü taraf sağlayıcılara yönlendirmesi bu akademik asistan oturumu için önerilmez.
