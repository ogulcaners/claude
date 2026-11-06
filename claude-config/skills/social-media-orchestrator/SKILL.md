---
name: social-media-orchestrator
description: Instagram ve sosyal medya yönetimini uçtan uca koordine eden meta-skill — hesap denetimi, strateji, aylık içerik takvimi, üretim, yayın öncesi kalite kapısı, topluluk yönetimi ve haftalık raporlama döngüsünü yürütür; hangi aşamada hangi skill'in ve alt ajanın (ig-analyst, ig-copywriter, ig-community-manager, ig-competitor-scout, ig-brand-reviewer) devreye gireceğine karar verir. "Instagram'ı yönet", "sosyal medya planı", "içerik takvimi", "hesabı büyüt", "haftalık rutin", "ne paylaşayım" taleplerinde ve hangi sosyal medya skill'inin tetikleneceği belirsizse kullan.
---

# Sosyal Medya Orkestratörü

Bu skill 5 uzman skill'i (`instagram-strategist`, `instagram-content-creator`, `instagram-analytics-reporter`, `instagram-community-manager`, `social-media-competitor-research`) ve 5 alt ajanı koordine eder. Kendisi derin içerik üretmez; **doğru aşamada doğru skill'i/ajanı tetikler** ve onay kapılarını işletir. Bağlayıcı kurallar: `~/.claude/CLAUDE.md` → "Instagram ve Sosyal Medya Çalışma Kuralları".

## İlk temas kontrol listesi

Kullanıcıyla ilk sosyal medya işinde sırayla sor/kontrol et (bilinenleri atla):
1. Hangi hesap(lar)? Business/Creator mı? Composio bağlı mı (`/mcp` listesinde composio "connected" mi)? Değilse `claude-config/docs/instagram-composio-kurulum.md`'ye yönlendir.
2. `brand/marka-rehberi.md` var mı? Yoksa `instagram-strategist` ile 15 dakikalık marka rehberi oturumu öner (hedef kitle, ses tonu, içerik sütunları, yasaklar, CTA'lar, rakipler).
3. Haftalık kapasite: kaç gönderi, kaç story, kim çekiyor/düzenliyor, hangi günler?
4. 90 günlük hedef: tek bir birincil KPI seç (ör. kaydetme oranı, profil ziyareti → takip dönüşümü, DM'den satış). Takipçi sayısı tek başına hedef olamaz.

## Yaşam döngüsü ve yönlendirme tablosu

| Aşama | Ritim | Ne yapılır | Skill | Ajan |
|---|---|---|---|---|
| 0. Kurulum | Bir kez | Composio bağlantısı, onay kuralı, marka rehberi | `instagram-strategist` | — |
| 1. Denetim | Bir kez + 3 ayda bir | Hesap denetimi, son 30-90 gün verisi, güçlü/zayıf içerik, rakip taban çizgisi | `instagram-analytics-reporter`, `social-media-competitor-research` | `ig-analyst`, `ig-competitor-scout` (paralel) |
| 2. Strateji | 90 günde bir | Konumlandırma, içerik sütunları (3-5), format karışımı, KPI hedefleri | `instagram-strategist` | — |
| 3. Aylık takvim | Ayda bir | 30 günlük plan: tarih, format, sütun, konu, kanca, CTA | `instagram-content-creator` | `ig-copywriter` |
| 4. Üretim | Haftalık toplu | Reels scripti, carousel, caption, hashtag, story dizisi | `instagram-content-creator` | `ig-copywriter` |
| 5. Kalite kapısı | Her içerik | Marka/doğruluk/platform/erişilebilirlik denetimi | — | `ig-brand-reviewer` |
| 6. Onay + yayın | Her içerik | Kullanıcı onayı → yayın (Composio) veya kullanıcı elle yayınlar | — | ana oturum (yalnızca onaylı) |
| 7. Topluluk | Günlük | DM/yorum triage ve taslak cevaplar | `instagram-community-manager` | `ig-community-manager` |
| 8. Rapor | Haftalık + aylık | KPI takibi, öğrenimler, sonraki haftanın ayarı | `instagram-analytics-reporter` | `ig-analyst` |

TaskCreate/TaskUpdate ile aktif döngüyü takip edilebilir bir liste yap; kullanıcı hangi aşamada olduğunu söylemezse önce bunu sor.

## Haftalık rutin (önerilen varsayılan)

| Gün | İş | Süre |
|---|---|---|
| Pazartesi | `ig-analyst` haftalık rapor → 3 öğrenim → bu haftanın takvim ayarı | 30 dk |
| Salı | `ig-copywriter` haftanın tüm içeriklerini toplu üretir (batch) | 60 dk |
| Çarşamba | `ig-brand-reviewer` denetim → düzeltmeler → kullanıcı onayı | 30 dk |
| Her gün | `ig-community-manager` DM/yorum triage (sabah + akşam) | 2×15 dk |
| Cuma | Rakip/trend taraması (`ig-competitor-scout`, 2 haftada bir) | 20 dk |
| Ay sonu | Aylık rapor + gelecek ay takvimi | 90 dk |

## Onay kapısı protokolü (zorunlu)

1. Taslaklar numaralanır (`T-2026-11-06-01`).
2. `ig-brand-reviewer` her taslağa `GEÇTİ`/`DÜZELT` verir; `DÜZELT` olan `ig-copywriter`'a döner.
3. Kullanıcıya **tek tek** sunulur: metin + görsel/video açıklaması + yayın saati + hashtag.
4. Kullanıcı `ONAYLANDI: T-...` yazmadan hiçbir Composio yazma aracı çağrılmaz. "Hepsini onayla" ifadesi listelenen taslaklar için geçerlidir; sonraki taslaklara taşınmaz.
5. DM/yorum cevapları için aynı kural; ayrıca 24 saat kuralı kontrol edilir.
6. Yayınlanan her içerik `calendar/YYYY-MM.md` dosyasına "yayınlandı + link + saat" olarak işlenir.

## Paralel çalıştırma kuralları

- Denetim aşamasında `ig-analyst` ve `ig-competitor-scout` **aynı anda** çalıştırılır (bağımsız).
- Üretim aşamasında birden fazla `ig-copywriter` örneği farklı içerik sütunları için paralel çalışabilir; hepsi aynı marka rehberini okur.
- `ig-brand-reviewer` ve `ig-copywriter` aynı taslak üzerinde sıralı çalışır (üret → denetle → düzelt).
- Alt ajanlar birbirini çağırmaz; koordinasyon ana oturumdadır.

## Çalışma dosyaları

| Klasör | İçerik | Sahip |
|---|---|---|
| `brand/marka-rehberi.md` | Ses tonu, kitle, sütunlar, yasaklar, CTA, rakip listesi | `instagram-strategist` |
| `calendar/YYYY-MM.md` | Aylık takvim ve yayın durumu | bu skill |
| `content/YYYY-MM-DD-<konu>.md` | Taslaklar (kanca varyantları, caption, hashtag, denetim sonucu) | `ig-copywriter` |
| `reports/instagram/YYYY-MM-DD-rapor.md` | Haftalık/aylık rapor | `ig-analyst` |
| `research/rakip-YYYY-MM-DD.md` | Rakip/trend araştırması | `ig-competitor-scout` |
| `inbox/YYYY-MM-DD-triage.md` | DM/yorum triage ve taslak cevaplar | `ig-community-manager` |

Bu klasörler `.gitignore`'dadır (kişisel veri ve taslak içerir).

## Kapı kontrolü: "aylık plan hazır" demeden önce

1. Her gün için format + sütun + konu + kanca + CTA dolu mu?
2. Format karışımı strateji ile uyumlu mu (ör. %50 Reels / %30 carousel / %20 tek görsel)?
3. Her sütun ayda en az 2 kez temsil ediliyor mu?
4. Kampanya/özel günler (`brand/marka-rehberi.md` takvimi) işlenmiş mi?
5. Üretim kapasitesini aşıyor mu? Aşıyorsa plan küçültülür, kullanıcıya bildirilir.

## Uyarı

Bu skill kendi başına strateji/içerik/analiz üretmez; her zaman ilgili uzman skill'i veya ajanı tetikler ve çıktıyı onay kapısı içinde konumlandırır. Yazma işlemi (paylaşım/DM) yalnızca kullanıcı onayıyla ve yalnızca ana oturumdan yapılır.
