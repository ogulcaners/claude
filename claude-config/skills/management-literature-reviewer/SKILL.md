---
name: management-literature-reviewer
description: Yönetim ve organizasyon (management & organization) alanında literatür taraması yürütür — araştırma sorusu tanımlama, TR/EN anahtar kelime üretme, dahil etme/dışlama ölçütleri, veritabanı tarama stratejisi, tekrar ayıklama, başlık/özet ve tam metin eleme, yöntem/bulgu çıkarma, tema/kurama göre sınıflandırma, literatür boşluğu tespiti ve APA 7 kaynakça üretimini kapsayan 14 adımlı iş akışını uygular. Kaynakların gerçekliğini Crossref/OpenAlex/Semantic Scholar ile doğrular, uydurma kaynak üretmez. "literatür taraması", "literature review", "systematic review", "kaynak taraması", "ilgili çalışmalar", "review yaz" gibi taleplerde kullan.
---

# Yönetim ve Organizasyon Literatür Taraması Uzmanı

Bu skill, İşletme Anabilim Dalı — Yönetim ve Organizasyon alanında bir literatür taraması yürütmek için tasarlanmıştır. Odak konular: örgüt teorileri, örgütsel davranış, liderlik, motivasyon, insan kaynakları yönetimi, stratejik yönetim, örgüt kültürü, örgütsel değişim, kurumsal teori, güç/politika/çatışma, yenilik ve girişimcilik.

Tüm akademik dürüstlük ve kaynak doğrulama kuralları `~/.claude/CLAUDE.md` dosyasında tanımlıdır ve bu skill için bağlayıcıdır — özellikle **kaynak/DOI uydurmama** ve **her kaynağı doğrulama** kuralları.

## 14 Adımlı İş Akışı

Kullanıcı bir literatür taraması istediğinde, bu adımları sırayla (TaskCreate ile takip edilebilir) uygula. Her adımın çıktısını kullanıcıyla paylaş, bir sonrakine geçmeden önce onay iste (özellikle adım 1-4 arası, çünkü taramanın kapsamını belirler).

1. **Araştırma problemini tanımla.** Kullanıcıyla birlikte net bir araştırma sorusu/sorunsalı yaz (PICO/SPIDER benzeri bir çerçeve management alanına uyarlanabilir: Popülasyon/bağlam, İlgi konusu kavram, Karşılaştırma/bağlam, Sonuç).
2. **Türkçe ve İngilizce anahtar kelimeleri oluştur.** Her ana kavram için TR + EN karşılığını listele.
3. **Eş anlamlıları ve alternatif kavramları belirle.** (ör. "örgütsel bağlılık" = "organizational commitment" = "affective/normative/continuance commitment"; "liderlik tarzı" = "leadership style" alt türleriyle: transformasyonel, hizmetkâr, otantik, paylaşılan liderlik vb.)
4. **Dahil etme ve dışlama ölçütlerini oluştur** (yayın yılı aralığı, dil, yayın türü — hakemli dergi/tez/kitap bölümü, ampirik/kavramsal, örneklem/bağlam sınırları).
5. **Akademik veri tabanlarında tarama yap.** Bu ortamda ücretli veritabanlarına (Scopus/WoS/EBSCO) VE çoğu durumda Crossref/OpenAlex/Semantic Scholar gibi API'lere doğrudan `WebFetch` erişimi de YOKTUR (ağ ilkesi engelliyor — bkz. `~/.claude/CLAUDE.md` Kaynak Doğrulama Protokolü). Bu nedenle tarama ve doğrulama **WebSearch** üzerinden yapılır: her aday kaynağı WebSearch ile ara, birden fazla bağımsız sonuçla (yayıncı sayfası + ikinci bir dizin/arşiv) çapraz doğrula. Kullanıcının kurumsal veritabanı erişimi varsa onun bulduğu kaynak listesini işlemeye hazır ol; farklı bir ortamda `WebFetch` API'lere ulaşabiliyorsa onu tercih et.
6. **Tekrarlanan kayıtları ayıkla** (başlık + DOI eşleştirmesiyle).
7. **Başlık ve özet elemesi yap** — dahil etme/dışlama ölçütlerine göre.
8. **Tam metin uygunluğunu değerlendir** (mümkünse; erişilemeyen tam metinler için bunu açıkça belirt, "erişilemedi" olarak işaretle, asla içeriğini uydurma).
9. **Kaynakların yöntem ve bulgularını çıkar** — her kaynak için: yöntem (nitel/nicel/karma, örneklem, veri toplama aracı), temel bulgular, kullanılan kuramsal çerçeve.
10. **Tema ve kuramlara göre sınıflandır** — bir tematik tablo/matris oluştur (kaynak × tema × kuram × bulgu).
11. **Literatürdeki boşlukları belirle** — hangi bağlamlar, örneklemler, kuramsal ilişkiler yeterince çalışılmamış.
12. **Kaynakların gerçekliğini doğrula** — bkz. `~/.claude/CLAUDE.md` "Kaynak Doğrulama Protokolü". Taramaya dahil edilen HER kaynak bu adımdan geçmeli.
13. **APA 7 kaynakça üret** (bkz. `academic-writer-apa7` skill'i).
14. **Çalışmanın sınırlılıklarını açıkça yaz** — taramanın kapsamı (hangi veritabanları/tarih aralığı taranabildi, hangi ücretli veritabanlarına erişilemedi, dil sınırlaması vb.).

## Çıktı Formatı

- Kısa bir **akış özeti** (kaç kaynak bulundu → tekrar ayıklandı → başlık/özet elendi → tam metin değerlendirildi → dahil edildi; PRISMA benzeri sayılarla).
- **Tematik/kuramsal sınıflandırma tablosu.**
- **Boşluk analizi** paragrafı.
- **APA 7 kaynakça** (yalnızca doğrulanmış kaynaklar).
- **Sınırlılıklar** paragrafı.

## Uyarılar

- Bu ortamda ücretli akademik veritabanlarına (Scopus, Web of Science, EBSCO) doğrudan erişim yoktur. Bunu kullanıcıya baştan belirt; taramanın Crossref/OpenAlex/açık erişim kaynaklarıyla sınırlı olduğunu ve kapsamlı bir sistematik derleme için kurumsal veritabanı erişimiyle tekrar kontrol edilmesi gerektiğini söyle.
- Asla "X makale bulundu" deme eğer gerçekten doğrulanmış X makale yoksa.
