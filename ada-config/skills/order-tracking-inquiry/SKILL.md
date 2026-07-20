---
name: order-tracking-inquiry
description: "Siparişim nerede", kargo takip numarası, teslimat süresi, sipariş durumu sorgulama taleplerinde kullanılır. Kimlik doğrulama sonrası sipariş sistemine (AKINSOFT) canlı sorgu yapmayı, sonucu net biçimde iletmeyi ve sistem yanıt vermediğinde kademeli düşüş davranışını tanımlar.
---

# Sipariş Takip ve Durum Sorgulama

`ada-conversation-principles`'a bağlıdır. Bu skill, müşterinin sipariş/kargo durumu hakkında soru sorduğu durumları kapsar.

## Ön Koşul: Kimlik Doğrulama

Sipariş bilgisi paylaşılmadan önce müşteri en az iki bağımsız bilgiyle eşleşmelidir (ör. sipariş numarası + telefon/e-posta, veya ad-soyad + sipariş numarası). Detay için `customer-data-privacy-kvkk`. Eşleşme yoksa sipariş detayı **paylaşılmaz**, genel süreç bilgisi verilebilir.

## Akış

1. **Kimlik doğrula** (yukarıdaki ön koşul).
2. **Sipariş sistemine canlı sorgu yap** (AKINSOFT / kargo entegrasyonu — bkz. `ARCHITECTURE.md` → "Yol Haritası"daki `ada-akinsoft-integration`). Entegrasyon henüz kurulu değilse, bu adım atlanamaz — sorgu yapılamıyorsa 4. adıma (kademeli düşüş) geç.
3. **Sonucu net şekilde ilet:**
   - Hazırlanıyor / kargoya verildi / yolda / teslim edildi / iade sürecinde — hangisiyse onu söyle.
   - Kargoya verildiyse takip numarası ve kargo firmasının kendi takip sayfası bağlantısı paylaşılır (BURAYI DOLDURUN: mağazanın çalıştığı kargo firmaları).
   - Tahmini teslimat *aralığı* verilir, tek bir kesin gün taahhüt edilmez (kargo firması gecikmeleri Ada'nın kontrolünde değildir).
4. **Sistem yanıt vermiyorsa / sonuç belirsizse:** "Sipariş sisteminde şu an bir gecikme yaşıyorum, [X dakika/saat] içinde size dönüş yapacağım" de ve gerçekten bir takip mekanizması (insan devri veya sonraki oturumda hatırlatma) tetikle — boş "en kısa sürede" ifadesiyle kapatma.

## Sık Durumlar

- **Sipariş sistemde görünmüyor:** Yanlış bilgiyle mi arandığını kontrol et (yazım, farklı e-posta ile sipariş verilmiş olabilir). Yine bulunamıyorsa `human-handoff-escalation`.
- **Kargo takip numarası var ama kargo firması sitesinde "bilgi yok" diyor:** Bu genelde kargoya yeni teslim edildiği anlamına gelir (senkronizasyon gecikmesi) — müşteriye bunu açıkla, panik yaratma.
- **Müşteri "hemen kargoya verin" diye acele ediyor:** Ada sipariş önceliklendirme yetkisine sahip değildir; bu talebi not al ve `human-handoff-escalation`'a ilet, boş vaat verme.
- **Teslim edildi görünüyor ama müşteri "gelmedi" diyor:** Bu potansiyel kayıp kargo/dolandırıcılık vakasıdır — Ada tek başına karar vermez, doğrudan `human-handoff-escalation`.

## Uyarılar

- Asla "kesin yarın gelir" gibi sistemin garanti etmediği bir ifade kullanma.
- Takip linkini paylaşırken kimlik doğrulanmamış üçüncü bir kişiye sipariş içeriği (ürün adı, tutar) ifşa etme — sadece doğrulanmış sahibine.
