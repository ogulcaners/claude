# Ada — Yapada Mağazası Müşteri Hizmetleri Asistanı

Bu dizin, yapadadukkan.com için geliştirilen **Ada** adlı müşteri hizmetleri odaklı yapay zeka asistanının prompt/skill mimarisini içerir. Mimari, [`arpitg1304/robotics-agent-skills`](https://github.com/arpitg1304/robotics-agent-skills) deposundaki `SKILL.md` tabanlı, seçici-kurulum destekli yapıdan esinlenilerek tasarlandı — gerekçe ve desen eşleştirmesi için `ARCHITECTURE.md`'ye bakın.

## Dizin Yapısı

```
ada-config/
├── CLAUDE.md          — Ada'nın kök sistem promptu: kimlik, skill yönlendirme tablosu, tüm skillerde bağlayıcı ortak kurallar
├── ARCHITECTURE.md    — Mimari tasarım kararları ve gerekçeleri (robotics-agent-skills eşleştirmesi, yol haritası)
├── install.sh         — Seçici skill kurulum scripti
├── skills/             — 8 adet SKILL.md formatlı müşteri hizmetleri skill'i
└── evals/              — Konuşma test senaryoları ve başarı kriterleri
```

## Skiller

| Skill | Ne zaman tetiklenir |
|---|---|
| `ada-conversation-principles` | Temel ilkeler — diğer tüm skillerin dayandığı taban |
| `order-tracking-inquiry` | Sipariş/kargo durumu sorgulama |
| `returns-refunds` | İade, değişim, cayma hakkı |
| `complaint-deescalation` | Öfkeli/şikayetçi müşteri |
| `product-inquiry-collectibles` | Ürün/stok/uyum soruları, ön satış tavsiyesi |
| `payment-issue-handling` | Ödeme hatası, çift çekim, taksit sorunu |
| `human-handoff-escalation` | Yetki/bilgi sınırı aşıldığında insana devir |
| `customer-data-privacy-kvkk` | Kimlik doğrulama, kişisel veri koruma |

Tam yönlendirme tablosu için `CLAUDE.md`'ye bakın.

## Kurulum

```bash
# Tam kapsam
./install.sh --target ~/.claude/skills --skills all

# Sadece temel müşteri hizmetleri (bkz. ARCHITECTURE.md → "Bundle Önerileri")
./install.sh --target ~/.claude/skills --skills ada-conversation-principles order-tracking-inquiry human-handoff-escalation customer-data-privacy-kvkk

# Mevcut skilleri listele
./install.sh --list
```

Kurulum sonrası, hedef ortamın ana `CLAUDE.md` dosyasına `ada-config/CLAUDE.md` içeriğinin (veya ona bir referansın) eklenmesi gerekir — skiller kendi başlarına Ada'nın kimliğini/ortak kurallarını içermez, kök `CLAUDE.md`'ye bağımlıdır.

## Bu Sistem Henüz Eksik Olan Neler İçeriyor

`ARCHITECTURE.md` → "Bilinçli Olarak Yazılmayanlar" ve "Yol Haritası" bölümlerinde detaylandırıldığı gibi, bu ilk sürüm **gerçek mağaza politikası verisi ve kanal/sistem entegrasyonu içermez** — bunlar `BURAYI DOLDURUN` notlarıyla işaretlendi. Ada'yı canlıya almadan önce:

1. Gerçek iade süresi/istisna listesi mağaza tarafından `returns-refunds` skill'ine girilmeli.
2. Kargo firması bilgileri `order-tracking-inquiry` skill'ine girilmeli.
3. AKINSOFT panel / sipariş / kargo / ödeme sistemine canlı sorgu entegrasyonu kurulmalı (`ARCHITECTURE.md` → Yol Haritası: `ada-akinsoft-integration`).
4. Hangi kanal(lar)da (WhatsApp, Instagram DM, site chat widget) çalışacağına karar verilip `ada-channel-integration` yazılmalı.
5. Canlıya almadan önce `evals/` altındaki test senaryolarıyla en az bir tur değerlendirme yapılmalı.

## Senkronizasyon

Bu dizin, kök `CLAUDE.md`'deki genel senkronizasyon kuralına tabidir: burada yapılan değişiklikler yalnızca commit edilirse kalıcı olur; canlı ortamda (`~/.claude/`) ayrıca kurulum (`install.sh`) çalıştırılmadıkça otomatik yansımaz.
