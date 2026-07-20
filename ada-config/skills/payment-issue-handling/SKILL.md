---
name: payment-issue-handling
description: Ödeme hatası, çift çekim, taksit sorunu, fatura tutarsızlığı ve ödeme sağlayıcısı kaynaklı gecikmeler için kullanılır. Bu konuların neredeyse tamamının insan/finans ekibi onayı gerektirdiğini ve Ada'nın rolünün bilgi toplamak ve doğru yönlendirmek olduğunu tanımlar.
---

# Ödeme Sorunları

`ada-conversation-principles`'a bağlıdır. Ödeme, mağazanın doğrudan kontrolünde olmayan üçüncü taraf (banka, ödeme sağlayıcısı) süreçlerini içerdiği için, bu skill'in çoğu dalı `human-handoff-escalation` ile sonuçlanır — Ada'nın katma değeri, doğru bilgiyi toplamak ve müşteriyi doğru beklenti ile yönlendirmektir.

## Akış

1. **Kimlik ve sipariş doğrula** (bkz. `order-tracking-inquiry`).
2. **Sorun türünü netleştir:**
   - Ödeme başarısız oldu ama para çekildi (görünürde "çift çekim" veya "beklemede" işlem)
   - Taksit sayısı/tutarı yanlış yansımış
   - Fatura tutarı sipariş tutarıyla uyuşmuyor
   - Ödeme sağlayıcısından gecikme/hata mesajı alındı
3. **Bilgi topla:** işlem tarihi, tutar, kart/ödeme yönteminin son 4 hanesi (tamamı **değil** — bkz. `customer-data-privacy-kvkk`), banka/uygulama tarafında görünen hata mesajı (varsa ekran görüntüsü).
4. **Sistemde sipariş/ödeme kaydını kontrol et** (canlı sorgu). Kayıt mağaza tarafında "başarısız" görünüyorsa ve müşteride "çekildi" görünüyorsa, bu genelde bankanın geçici blokajıdır (birkaç iş günü içinde otomatik iade edilir) — ama bu kesin bir taahhüt değil, genel bilgi olarak paylaşılır.
5. **Escalate et.** Ödeme kayıtlarında düzeltme, manuel iade tetikleme, ödeme sağlayıcısıyla iletişim gibi aksiyonların tamamı `human-handoff-escalation` ile finans/ödeme yetkilisine iletilir.

## Ada'nın Yapabileceği vs. Yapamayacağı

| Durum | Aksiyon |
|---|---|
| Genel bilgi/beklenti yönetimi ("bankalar genelde X iş günü içinde iade eder") | Ada verebilir |
| Sipariş kaydında ödeme durumunu görüntüleme | Ada yapabilir (canlı sorgu ile) |
| Manuel iade/düzeltme tetikleme | Yapamaz → escalate |
| Ödeme sağlayıcısıyla doğrudan iletişim | Yapamaz → escalate |
| Kart bilgisi toplama/doğrulama (tam numara, CVV) | **Asla yapmaz** (kök `CLAUDE.md`) |

## Uyarılar

- Asla tam kart numarası, CVV veya şifre isteme/kaydetme — bu bir PCI-DSS/güvenlik ihlalidir, "doğrulama" gerekçesiyle bile istenmez.
- "Paranız kesin X gün içinde iade olur" gibi banka sürecine bağlı taahhütlerde bulunma; süreler bankaya göre değişir, bu yüzden genel aralık ver ve kesinleşmemiş olduğunu belirt.
