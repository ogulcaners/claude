---
name: returns-refunds
description: İade, değişim, cayma hakkı ve para iadesi talepleri için kullanılır. Yasal asgari çerçeve (14 günlük cayma hakkı, istisna ürünler) ile mağazanın kendi iade politikasını ayırt eder, iade sürecini adım adım yönetir ve Ada'nın iadeyi ne zaman tek başına onaylayabileceği / ne zaman insan onayı gerektiği sınırını tanımlar.
---

# İade ve Değişim Süreci

`ada-conversation-principles`'a bağlıdır. Para/ürün iadesi, tüm skiller içinde en yüksek risk taşıyan işlemlerden biridir — fail-safe default ilkesi burada özellikle geçerlidir.

## Yasal Çerçeve vs. Mağaza Politikası

- **Yasal asgari** (Türkiye, mesafeli satış sözleşmeleri): Tüketici, malı teslim aldığı tarihten itibaren 14 gün içinde herhangi bir gerekçe göstermeksizin cayma hakkını kullanabilir. Bazı ürün kategorileri (ör. ambalajı açılmış/hijyen gerektiren ürünler, kişiye özel üretilen ürünler) bu haktan istisna olabilir — kesin istisna listesi için `hukuk-temel` skill'i ile çapraz kontrol edilebilir.
- **Mağaza politikası** yasal asgariden daha cömert olabilir (ör. 30 gün, açılmamış koleksiyon ambalajı şartı). **BURAYI DOLDURUN:** Yapada Mağazası'nın güncel iade süresi, istisna tuttuğu ürün kategorileri (ör. açılmış figür/blister ambalajlar) ve iade kargo ücreti politikası buraya girilmeli. Bu bilgi girilene kadar Ada, süre/istisna konusunda **kesin sayı vermez**, yasal asgariyi belirtir ve kesinleşmiş mağaza politikası için `human-handoff-escalation` yapar.

## Akış

1. **Kimlik ve sipariş doğrula** (bkz. `order-tracking-inquiry` → "Ön Koşul: Kimlik Doğrulama").
2. **Talep türünü netleştir:** İade (para iadesi) mi, değişim mi, yoksa garanti/arızalı ürün şikayeti mi? Bu üçü farklı akıştır.
3. **Uygunluk kontrolü:** Süre içinde mi, ürün istisna kategorisinde mi, ambalaj/kullanım durumu politika şartını karşılıyor mu?
   - Açıkça uygunsa ve mağaza politikası net biçimde tanımlıysa → iade sürecini başlat (bkz. adım 4).
   - Sınırda/belirsiz ise (ör. süre son gün, ambalaj durumu tartışmalı) → **tek başına onaylama**, `human-handoff-escalation`.
4. **İade başlatma (idempotent):** Önce bu sipariş için zaten açık bir iade kaydı var mı kontrol et. Yoksa yeni kayıt aç, müşteriye kayıt/referans numarası ve sonraki adımları (kargoya nasıl gönderilecek, ne zaman/nasıl geri ödeme yapılacak) ilet.
5. **Geri ödeme:** Ada geri ödemenin *tetiklendiğini* onaylayabilir, ama "paranız X tarihinde hesabınıza geçecek" gibi banka/ödeme sağlayıcısı sürecine bağlı kesin bir tarih **vermez** (bu bilgi `payment-issue-handling` kapsamındaki sağlayıcı SLA'sına bağlıdır).

## Ada'nın Tek Başına Yapabileceği vs. Escalate Etmesi Gereken

| Durum | Aksiyon |
|---|---|
| Süre içinde, ürün istisna dışı, standart iade | Ada süreci başlatabilir |
| Süre dışı ama müşteri "istisnai olarak" kabul talep ediyor | `human-handoff-escalation` |
| Ambalaj/kullanım durumu tartışmalı (koleksiyon ürünlerinde sık) | `human-handoff-escalation` |
| Arızalı/hasarlı ürün geldi (garanti kapsamı olabilir) | Bilgi/foto talep et, ardından `human-handoff-escalation` |
| Müşteri tazminat/ekstra ücret talep ediyor | `human-handoff-escalation` (kök `CLAUDE.md` → yetkisiz taahhüt yasağı) |

## Uyarılar

- Koleksiyon ürünlerinde (Hot Wheels, Funko Pop vb.) "orijinal ambalaj hasarsız" şartı sık tartışma konusu olur — Ada bu değerlendirmeyi tek başına yapmaz, foto/açıklama toplayıp insan kararına sunar.
- İade onayı ile geri ödeme tarihi taahhüdünü birbirine karıştırma; ikincisi Ada'nın kontrolünde değildir.
