# CapCut MCP Sunucuları — Güvenlik Denetimi (2026-11-05)

CapCut'ın herkese açık resmî bir API'si veya MCP sunucusu yok; claude.ai connector dizininde de CapCut bulunamadı. Aşağıdaki 5 topluluk deposu `git clone --depth 1` ile alınıp salt-okunur incelendi (Read/Grep). Hiçbir kurulum veya script çalıştırılmadı.

Tüm adayların ortak sınırı: hepsi **CapCut taslak (draft) klasörü** üretir. Taslak ancak kullanıcının kendi bilgisayarında kurulu CapCut masaüstü uygulamasında açılabilir. Bu bulut oturumunda CapCut yok; bu yüzden hiçbiri burada uçtan uca işe yaramaz. Taslak formatı resmî olmayan, CapCut sürümleri arasında değişen bir formattır.

## Depo Bazında Özet

| Depo | Tür | Karar | Gerekçe |
|---|---|---|---|
| sun-guannan/VectCutAPI | Bireysel/ticari bağlantılı (Python, Apache-2.0) | **Kurulmadı — veri sızıntısı riski** | Yerel HTTP sunucusu `127.0.0.1:9001`'e bağlanıyor (iyi), fakat `query_script`/`download_script` yolu taslak kimliğini sabit kodlu harici bir sunucuya (`cut-jianying-…cn-hongkong.fcapp.run`) gönderiyor; `mcp_server.py` her taslak için üçüncü taraf bir alan adına (`install-ai-guider.top`) link üretiyor; `config.json` varsayılan alanı `capcutapi.top` (yazarın ücretli bulut hizmeti). `is_upload_draft` açılırsa taslaklar Aliyun OSS'e yükleniyor (varsayılan kapalı). `desktop_companion.py` `shell=True` ile süreç başlatıyor. Kod büyük (176 dosya) ve yerel/uzak yollar iç içe. |
| Atx-Guy/capcut-mcp-server | Bireysel (TypeScript) | Kurulmadı | VectCutAPI'nin ince bir sarmalayıcısı (VectCutAPI'yi çalıştırmayı gerektirir → yukarıdaki risk devralınır). LICENSE dosyası yok (yalnızca `package.json`'da "MIT"). Kod VectCutAPI içindeki `mcp-server/` klasörüyle neredeyse birebir aynı. |
| MigueDuque/capcut-mcp-server-extended | Bireysel fork (Node + Python, MIT) | Kurulmadı | Atx-Guy fork'u; VectCutAPI bağımlılığı aynen geçerli. Depoya derlenmiş `__pycache__/*.pyc` dosyaları commit edilmiş (kaynakla eşleştiği doğrulanamaz — tedarik zinciri uyarısı). Ağ çağrıları yalnızca `localhost:9001`'e. |
| yeroshalmiariel-ai/capcut-mcp | Bireysel (Python, MIT, v0.1.0) | **Kurulmadı burada — en temiz aday, kullanıcının kendi bilgisayarı için değerlendirilebilir** | Harici sunucuya hiçbir ağ çağrısı yok; taslağı doğrudan diske yazar (`pyJianYingDraft` ile). HTTP modu varsayılan `127.0.0.1`; uzak erişimde parola + OAuth zorunlu, `hmac.compare_digest`, deneme sınırı, yönlendirme host beyaz listesi var. Var olan taslağın üzerine yazmak için açık `replace=true` ister. Testler ve 3 işletim sistemli CI var. Uyarı: çok yeni/erken sürüm, topluluk denetimi az; ByteDance ile ilişkisi yok. |
| GuanYixuan/pyJianYingDraft | Kütüphane (Python, Apache-2.0) | Bağımlılık olarak not edildi | Yukarıdaki aday bunu kullanıyor. Çalışma zamanında ağ çağrısı bulunmadı. Esas olarak Çince JianYing için yazılmış; CapCut (uluslararası) desteği ayrı bir depoda "geliştirme aşamasında". Bazı özellikler eski JianYing sürümleriyle sınırlı. |

## Karar

- Bu bulut ortamına **hiçbir CapCut MCP sunucusu kurulmadı** (CapCut uygulaması olmadan işe yaramaz).
- VectCutAPI tabanlı üç seçenek (VectCutAPI, Atx-Guy, MigueDuque) **önerilmez**: taslak verisinin üçüncü taraf sunuculara gidebildiği kod yolları var.
- Kullanıcı kendi bilgisayarında CapCut kullanıyorsa ve otomasyon isterse: `yeroshalmiariel-ai/capcut-mcp` **stdio modunda** (HTTP/tünel açmadan), sabit bir commit'e kilitlenerek ve önce bir test taslağıyla denenebilir.
- Önerilen bağlantısız alternatif: ElevenLabs'te ses üret → dosyaları CapCut'a elle aktar; kurgu planı/altyazı metni Claude tarafından hazırlanır.
