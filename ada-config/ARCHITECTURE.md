# Ada Sistem Mimarisi

Bu doküman, Ada'nın skill/prompt mimarisinin nereden geldiğini ve neden bu şekilde tasarlandığını kaydeder — tıpkı kök depodaki `claude-config/AUDIT-REPORT-2026-07-17.md`'nin akademik skill kararlarını kaydetmesi gibi, bu da Ada'nın mimari kararlarını kaydeder.

## Referans Alınan Kaynak

Mimari, [`arpitg1304/robotics-agent-skills`](https://github.com/arpitg1304/robotics-agent-skills) deposundan esinlenildi (incelendi: 2026-07-20). O depo, ROS/robotik yazılım geliştirme için Claude Code/Cursor/Copilot ajanlarına yönelik 10 adet `SKILL.md` formatlı bilgi modülü sunuyor. Ada'nın domaini (müşteri hizmetleri) tamamen farklı, ama o deponun **yapısal desenleri** doğrudan uygulanabilir bulundu:

| robotics-agent-skills deseni | Ada'ya uyarlanışı |
|---|---|
| `skills/<isim>/SKILL.md` — her skill kendi klasöründe, tek dosya | Aynen korundu: `ada-config/skills/<isim>/SKILL.md` |
| `robotics-software-principles` — tüm diğer skillerin dayandığı 12 tasarım ilkesi | `ada-conversation-principles` — Ada'nın tüm skillerinin dayandığı ortak ilkeler (fail-safe default, idempotency, gözlemlenebilirlik, kademeli düşüş, vb. — bkz. kök `ada-config/CLAUDE.md`) |
| `install.sh --target <path> --skills <isim1> <isim2>` — seçici kurulum | Aynı desen: `ada-config/install.sh` |
| Önerilen "bundle"lar (ör. "production systems" = ros2 + robot-bringup + robotics-security + robotics-testing) | Aşağıdaki "Bundle Önerileri" bölümü |
| `evals/` — skill açık/kapalıyken karşılaştırmalı kalite ölçümü | `ada-config/evals/` — konuşma senaryoları ve başarı kriterleri (bkz. o klasördeki README) |
| Apache-2.0 + `CONTRIBUTING.md` ile katkı süreci | Ada özelinde uygulanmadı — bu depo tek kullanıcı/tek mağaza için, açık katkı süreci şimdilik gereksiz görüldü |
| Roadmap bölümü (planlanan ama henüz yazılmamış skiller) | Aşağıdaki "Yol Haritası" bölümünde tutuluyor |

**Neden bu desen benimsendi:** robotics-agent-skills'in temel önermesi — "genel amaçlı ajanlar sözdizimini bilir ama üretimde önemli olan alan-özel detayları kaçırır" — müşteri hizmetleri için de geçerli. Genel bir LLM, Türkçe nazik cümleler kurabilir ama *ne zaman insana devretmesi gerektiğini*, *hangi veriyi asla uydurmaması gerektiğini* veya *KVKK kapsamında hangi kişisel veriyi isteyip isteyemeyeceğini* bilmez. Bu yüzden robotics-agent-skills'teki "safety isn't optional, it's the baseline" ilkesi, Ada'da "escalation ve doğrulama isteğe bağlı değil, varsayılandır" ilkesine dönüştü.

## Skill Envanteri

| Skill | Robotik dünyasındaki analoğu | Odak |
|---|---|---|
| `ada-conversation-principles` | `robotics-software-principles` | Tüm skillerin dayandığı temel ilkeler |
| `order-tracking-inquiry` | `robot-perception` (sensör/durum okuma) | Sipariş/kargo durumu sorgulama |
| `returns-refunds` | `robotics-design-patterns` (FSM/durum yönetimi) | İade/değişim akışı, durum makinesi |
| `complaint-deescalation` | — (domain'e özgü, analog yok) | Öfkeli müşteri, ton yönetimi |
| `product-inquiry-collectibles` | `robot-perception` | Ürün/stok/uyum soruları |
| `payment-issue-handling` | `robotics-security` (kritik/hassas işlemler) | Ödeme hatası, çift çekim |
| `human-handoff-escalation` | `robot-bringup` (graceful shutdown/devir) | İnsana devir protokolü |
| `customer-data-privacy-kvkk` | `robotics-security` | Kişisel veri, kimlik doğrulama |

Not: robotics-agent-skills'teki `ros1`/`ros2` (platform-özel API bilgisi) ve `docker-ros2-development`/`ros2-web-integration` (deployment) skillerinin Ada'daki karşılığı henüz yazılmadı — bkz. "Yol Haritası". Bunlar Ada'nın *hangi platformlarda* (WhatsApp, Instagram DM, site chat widget'ı, AKINSOFT panel entegrasyonu) çalışacağına bağlı, ve bu netleşmeden yazılırsa varsayımsal/hayali entegrasyon detayı üretme riski var.

## Bundle Önerileri

Kurulum sırasında (`install.sh`) hangi skill kombinasyonunun birlikte kullanılacağına dair öneriler:

- **Temel müşteri hizmetleri (minimum):** `ada-conversation-principles` + `order-tracking-inquiry` + `human-handoff-escalation` + `customer-data-privacy-kvkk`
- **Tam kapsam (önerilen):** yukarıdakiler + `returns-refunds` + `complaint-deescalation` + `product-inquiry-collectibles` + `payment-issue-handling`
- **Sadece ön-satış asistanı** (henüz sipariş sonrası destek yoksa): `ada-conversation-principles` + `product-inquiry-collectibles` + `human-handoff-escalation`

## Bilinçli Olarak Yazılmayanlar

Aşağıdakiler bilinçli olarak bu ilk sürüme dahil edilmedi çünkü gerçek, doğrulanmış mağaza-özel veri gerektiriyor ve bu veri olmadan yazmak "uydurma" ilkesini ihlal eder:

- Gerçek iade süresi/istisna listesi (yasal asgari 14 gün cayma hakkı dışında — mağazanın kendi politikası girilmeli)
- Kargo firması adları/SLA'ları
- Ödeme sağlayıcısı entegrasyon detayları
- Instagram/WhatsApp/web chat kanal entegrasyon kodları

Bu boşluklar ilgili skill dosyalarında `BURAYI DOLDURUN` notlarıyla işaretlendi.

## Yol Haritası

Planlanan ama henüz yazılmamış skiller (robotics-agent-skills'teki "Roadmap" bölümüne benzer şekilde, buraya not düşülüyor):

- `ada-channel-integration` — hangi mesajlaşma kanalı(ları) kullanılacaksa (WhatsApp Business API, Instagram DM, site chat widget) o kanala özel format/kısıt bilgisi
- `ada-akinsoft-integration` — AKINSOFT panel sorgu/aksiyon protokolü (sipariş, stok, iade durumu okuma/yazma)
- `ada-conversation-testing` — `evals/` klasörünü besleyecek, robotics-agent-skills'teki `robotics-testing`'in karşılığı: test senaryosu şablonları, red-team promptları, regresyon kontrolü

Bu üçü, gerçek entegrasyon detayları (API uç noktaları, kimlik bilgileri, kanal seçimi) netleştiğinde yazılmalı — şimdiden yazmak varsayımsal/hatalı entegrasyon varsayımlarına yol açar.
