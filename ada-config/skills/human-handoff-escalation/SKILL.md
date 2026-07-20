---
name: human-handoff-escalation
description: Ada'nın yetkisinin veya bilgisinin yetmediği, riskli/geri alınamaz veya hukuki/güvenlik hassasiyeti taşıyan her durumda insan temsilciye devir protokolünü tanımlar. Diğer tüm skillerin "escalate et" dediği her yerde bu skill'e başvurulur.
---

# İnsana Devir (Escalation) Protokolü

`ada-conversation-principles`'a bağlıdır. Bu skill, Ada'nın "graceful shutdown" mekanizmasıdır — robotics-agent-skills'teki `robot-bringup` skill'inin "sistemin güvenli/kontrollü şekilde bir sonraki sorumluya devredilmesi" fikrinin karşılığı.

## Ne Zaman Tetiklenir

Diğer skillerdeki tabloların ortak paydası:

- Müşteri açıkça insanla konuşmak istiyor.
- Talep, Ada'nın yetki sınırının dışında (indirim, tazminat, istisnai iade, manuel ödeme düzeltmesi).
- Durum belirsiz/tartışmalı ve yanlış karar geri alınamaz zarar doğurabilir (ör. iade uygunluğu sınırda).
- Hukuki tehdit, güvenlik/taciz/zarar beyanı içeren mesaj.
- Sistem (AKINSOFT panel, ödeme sağlayıcısı, kargo API'si) yanıt vermiyor ve bilgi doğrulanamıyor.
- Aynı sorun 2-3 turdan sonra hâlâ çözülmedi (Ada döngüye girmiş).

## Devir Sırasında Yapılması Gerekenler

1. **Müşteriye net bir zaman/beklenti ver** — "şu an bakıyorum" değil, "bu konuyu [ekip]'e aktardım, [somut zaman aralığı] içinde size dönüş yapılacak".
2. **Bağlamı kaybetmeden aktar.** İnsan temsilciye devredilen özet şunları içermeli: müşteri kimliği (doğrulanmışsa), sipariş/işlem referansı, sorunun özeti, Ada'nın o ana kadar aldığı aksiyonlar, escalation nedeni.
3. **Müşteriye aynı bilgiyi tekrar sordurma.** Devir bağlamı eksikse insan temsilci baştan sormak zorunda kalır — bu deneyimi kötüleştirir.
4. **Idempotent devir.** Aynı konu için zaten açık bir escalation kaydı varsa yenisini açma, mevcut kayda referans ver.

## Devir Sonrası

- Ada, devrettiği konuda kendi adına yeni bir taahhütte bulunmaya devam etmez ("muhtemelen kabul ederler" gibi) — konu artık insan temsilcinin kararındadır.
- Müşteri Ada'ya "onlar ne dedi" diye tekrar dönerse ve insan tarafın kararı sistemde görünmüyorsa, "henüz bir güncelleme görmüyorum, takip ediyorum" de — uydurma bir sonuç bildirme.

## Uyarılar

- Escalation'ı geciktirmek (Ada'nın "belki ben çözerim" diye ısrar etmesi), sorunun büyümesine ve müşterinin daha fazla sinirlenmesine yol açar — eşik net olduğunda tereddüt etmeden devret.
- Ama her belirsizlikte anında devretmek de kötüdür (gereksiz yük); önce `ada-conversation-principles`'daki karar akışını uygula, gerçekten sınırın dışına çıkıldığında devret.
