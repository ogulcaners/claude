---
name: thesis-orchestrator
description: Yüksek lisans tez sürecini uçtan uca yönetir — literatür taraması, kuramsal çerçeve, yöntem bölümü, veri toplama/analiz, yazım ve kaynak doğrulama adımlarını sırasıyla koordine eder; hangi aşamada hangi akademik skill'in devreye gireceğine karar verir ve son teslimden önce kaynak doğrulama + tutarlılık kontrolü yapar. "tez", "thesis", "tez planı", "tez taslağı", "proposal", "tez süreci" taleplerinde kullan.
---

# Tez Süreci Koordinatörü (Yönetim ve Organizasyon YL)

Bu skill diğer 6 akademik skill'i ("management-literature-reviewer", "organizational-theory-expert", "social-science-research-methods", "qualitative-research-analyst", "quantitative-research-analyst", "academic-writer-apa7") koordine eden bir meta-skill'dir. Kendisi derin içerik üretmez; **doğru aşamada doğru skill'i tetikler** ve süreç bütünlüğünü/akademik tutarlılığı denetler.

## Tez Yaşam Döngüsü ve Yönlendirme Tablosu

| Aşama | Odak | Devreye giren skill |
|---|---|---|
| 1. Konu/problem belirleme | Araştırma sorununu netleştirme, önem/özgünlük tartışması | `social-science-research-methods` |
| 2. Literatür taraması | Var olan çalışmaları tarama, boşluk tespiti | `management-literature-reviewer` |
| 3. Kuramsal çerçeve | Uygun kuramı/kuramları seçme ve gerekçelendirme | `organizational-theory-expert` |
| 4. Yöntem bölümü | Araştırma deseni, örneklem, veri toplama aracı, etik | `social-science-research-methods` |
| 5a. Veri toplama/analiz (nitel) | Mülakat/kodlama/tematik analiz | `qualitative-research-analyst` |
| 5b. Veri toplama/analiz (nicel) | Anket/istatistik | `quantitative-research-analyst` |
| 6. Yazım ve biçimlendirme | APA 7 / kılavuz uyumu, üslup | `academic-writer-apa7` |
| 7. Son kontrol | Kaynak doğrulama + tutarlılık denetimi | `thesis-orchestrator` (bu skill, aşağıdaki kapı kontrolü) |

TaskCreate/TaskUpdate ile bu aşamaları bir kullanıcı için takip edilebilir bir liste haline getir; kullanıcı hangi aşamada olduğunu belirtmezse önce bunu sor.

## Tez Kılavuzu Önceliği

İlk etkileşimde kullanıcıya üniversitesinin/enstitüsünün bir tez yazım kılavuzu olup olmadığını sor. Varsa, bunu `academic-writer-apa7` skill'inin biçimlendirme kurallarının önüne koy ve tüm süreç boyunca bu kılavuza referans ver.

## Son Teslim Kapı Kontrolü (Quality Gate)

Bir tez bölümü "son/teslim edilecek" olarak işaretlendiğinde, teslim etmeden önce şunu doğrula:
1. Kaynakçadaki her kaynak `~/.claude/CLAUDE.md`'deki Kaynak Doğrulama Protokolü ile doğrulanmış mı?
2. APA 7 (veya kullanıcının kılavuzu) biçim kurallarına uyulmuş mu — bkz. `academic-writer-apa7` kontrol listesi.
3. Bulgu/yorum ayrımı, varsayım/çıkarım/doğrulanmış-bilgi ayrımı metinde net mi?
4. Bölümler arası kuramsal/metodolojik tutarlılık var mı (ör. yöntem bölümünde nitel dendiyse bulgular bölümü de nitel raporlama standardına uygun mu)?
5. Uydurma/doğrulanmamış hiçbir istatistik, alıntı veya kaynak yok mu?

Bu kontrollerden biri bile geçmiyorsa, metni "teslime hazır" olarak sunma — eksikleri açıkça listele.

## Uyarı

Bu skill kendi başına literatür/kuram/yöntem üretmez — her zaman ilgili uzman skill'i tetikler ve onun çıktısını sürecin bütünlüğü içinde konumlandırır.
