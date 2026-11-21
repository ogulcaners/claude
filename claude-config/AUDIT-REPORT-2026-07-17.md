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

## Ek Değerlendirme — 2026-07-27: diegosouzapw/OmniRoute

Kullanıcı bu depoyu paylaşıp `claude-config`'e bir şey taşınıp taşınamayacağını sordu. Salt-okunur inceleme (repo `add_repo` ile bu oturuma eklenemedi — farklı sahiplik katmanı; bunun yerine genel GitHub sayfaları/raw dosyalar WebFetch ile incelendi).

**Ne olduğu:** OmniRoute bir Claude skill'i veya MCP sunucusu değil — 290+ sağlayıcıyı (OpenAI, Anthropic, Bedrock vb.) tek bir yerel uç noktada (`http://localhost:20128/v1`) birleştiren, token sıkıştırma ve otomatik yönlendirme yapan bağımsız bir Node.js/Next.js AI gateway sunucusudur. Kendi `CLAUDE.md` dosyası da bu depoya katkıda bulunacak geliştiriciler için bir mühendislik rehberidir (worktree kuralları, güvenlik kuralları, test zorunluluğu) — kullanıcının akademik asistanına kopyalanabilecek bir şey değildir.

**Karar: Hiçbir şey taşınmadı/kurulmadı.** Gerekçe:
1. **Kategori uyuşmazlığı** — `claude-config/skills/` yapısı akademik iş akışı skill'lerinden oluşuyor; OmniRoute bir geliştirici altyapı/proxy aracı. Tez/literatür/APA7/kaynak doğrulama süreciyle hiçbir ilgisi yok.
2. **Güven sinyalleri karışık** — MIT lisanslı ve kendi `CLAUDE.md`'sinde ciddi güvenlik kuralları (hata mesajı sanitizasyonu, Zod doğrulama, PII redaksiyonunun varsayılan kapalı olması) var; ancak tek kişilik bir GitHub hesabında (`diegosouzapw`) 31,2k yıldız / 4k fork, "500+ katkıda bulunan" ve "Kimi (Moonshot AI) destekli" iddiaları bulunuyor ve bu iddialar doğrulanamadı (contributors grafiği yüklenemedi). Bu kalıp, yukarıdaki tabloda `Imbad0202/academic-research-skills` için işaretlenen "istatistiksel olarak anormal yıldız oranı" güven riskiyle aynı.
3. **Güven yüzeyi çok daha geniş** — Kurulumu, kullanıcının TÜM AI sağlayıcı trafiğini (Claude Code dahil) yerel bir üçüncü-taraf proxy üzerinden geçirmesini, `JWT_SECRET`/`API_KEY_SECRET` gibi kimlik bilgilerini saklamasını ve bir `postinstall` betiği çalıştırmasını gerektiriyor (betiğin kendisi zararsız görünüyor — `better-sqlite3` runtime'ını önceden çözümlüyor — ama npm `postinstall` genel olarak tedarik zinciri riski taşıyan bilinen bir vektördür). Bu, şimdiye dek incelenen herhangi bir akademik MCP sunucusundan çok daha büyük bir blast radius.
4. **Bu oturumun kapsamı dışında** — Ayrıca bu, yerel makinede (kullanıcının kendi bilgisayarında) çalıştırılacak bağımsız bir sunucu; bu geçici bulut oturumunda kurulup çalıştırılması zaten anlamsız (54yyyu/zotero-mcp kaydındaki mantığın aynısı).

**Kullanıcı için not:** Maliyet optimizasyonu / çoklu sağlayıcı yönlendirmesi için böyle bir gateway kullanmak isterse, bu ayrı ve bağımsız bir karar olmalı — kimlik bilgisi saklama ve `postinstall` yüzeyini kendi makinesinde, güncel bağımlılık/CVE taramasıyla birlikte değerlendirmesi önerilir. Akademik asistan yapılandırmasının bir parçası değildir.
