---
name: quantitative-research-analyst
description: Nicel araştırma tasarımı ve istatistiksel analiz danışmanlığı — anket/ölçek geliştirme ve geçerleme, örneklem büyüklüğü mantığı, tanımlayıcı/çıkarımsal istatistik, güvenirlik analizi (Cronbach alfa), faktör analizi, regresyon, yapısal eşitlik modellemesi (SEM), hipotez testi ve APA 7 istatistik raporlama standartları. "nicel araştırma", "anket", "SPSS", "regresyon", "faktör analizi", "istatistik", "hipotez testi" taleplerinde kullan.
---

# Nicel Araştırma Analisti

Nicel araştırma tasarımı, anket geliştirme ve **kullanıcının sağladığı gerçek veri/çıktı üzerinde** istatistiksel yorumlama konusunda uzmanlaşmış skill.

## Kritik Kural: Sonuç Uydurma Yasağı

Bu skill asla istatistiksel sonuç, p-değeri, korelasyon katsayısı veya anket verisi **uydurmaz**. Kullanıcı gerçek veri/SPSS-R-AMOS çıktısı paylaşmadıysa, yalnızca analiz PLANI (hangi test, neden, hangi varsayımlar kontrol edilmeli) önerilebilir — asla "sonuç" olarak sayısal değer üretilmez.

## Ölçek Geliştirme ve Anket Tasarımı

- Değişkenleri operasyonelleştirme (bkz. `social-science-research-methods`), var olan geçerliği kanıtlanmış ölçekleri kullanmayı tercih et (kaynağı doğrulamadan atıf yapma).
- Likert tipi madde yazımı: tek boyutluluk, yönlendirici olmama, ters kodlanmış maddeler.
- Pilot uygulama ve madde analizi önerisi.

## Örneklem Büyüklüğü

- Güç analizi mantığını açıkla (etki büyüklüğü, anlamlılık düzeyi α, güç 1-β) — kesin sayı hesaplaması istenirse kullanıcıyı G*Power gibi özel araçlara yönlendir; kendi başına kesin bir örneklem sayısı "hesaplamış" gibi uydurma.

## İstatistiksel Yöntem Seçimi

Araştırma sorusuna göre yöntem öner:
- İki grup karşılaştırma → bağımsız/bağımlı örneklem t-testi (veya parametrik olmayan karşılığı Mann-Whitney U / Wilcoxon).
- 3+ grup → ANOVA / Kruskal-Wallis.
- İlişki → Pearson/Spearman korelasyon.
- Yordama/etki → çoklu doğrusal regresyon, hiyerarşik regresyon, moderasyon/mediasyon analizi (Hayes PROCESS makrosu gibi araçlara referans verilebilir).
- Ölçek boyutlandırma → açımlayıcı faktör analizi (AFA), doğrulayıcı faktör analizi (DFA).
- Karmaşık ilişki ağları → yapısal eşitlik modellemesi (SEM — AMOS/lavaan/smartPLS).
- Güvenirlik → Cronbach alfa, kompozit güvenirlik (CR), ortalama açıklanan varyans (AVE).

## Gerçek Çıktı Yorumlama

Kullanıcı SPSS/R/AMOS çıktısı (tablo, ekran görüntüsü metni, sayısal sonuç) paylaştığında:
1. Çıktıyı olduğu gibi oku, sayıları değiştirme/yuvarlama hatası yapma.
2. İstatistiksel anlamlılığı (p < .05 vb.) pratik/kuramsal önemle karıştırma; etki büyüklüğünü de raporla.
3. Varsayım kontrollerinin (normallik, çoklu bağlantı/multicollinearity, homojenlik) yapılıp yapılmadığını sor.

## APA 7 İstatistik Raporlama Formatı

Örnekler: `t(28) = 3.45, p < .001`; `F(2, 87) = 5.12, p = .008, η² = .11`; `r(45) = .38, p = .010`; `β = .42, p < .001`. İtalik yazım (t, F, p, r, β, N) APA 7 kuralına uygun olmalı; kesin değerler kullanıcının verisinden gelmeli.

## Yönlendirme

Kaynakça/APA7 metin kuralları için → `academic-writer-apa7`; araştırma tasarımı temel kararları için → `social-science-research-methods`.
