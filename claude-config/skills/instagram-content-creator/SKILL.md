---
name: instagram-content-creator
description: Instagram içerik üretimi — Reels scripti (kanca kütüphanesi, beat yapısı, altyazı/kapak notu), carousel slayt metinleri, caption yapısı, 3 katmanlı hashtag seti, story dizisi, aylık içerik takvimi; marka rehberine ve içerik sütunlarına bağlı kalır. "Reels yaz", "kanca üret", "caption hazırla", "carousel yap", "hashtag", "story dizisi", "içerik takvimi", "30 günlük plan", "bu hafta ne paylaşayım" taleplerinde kullan. Marka-özel Yapada hesapları için önce yapada-instagram skill'ine bak.
---

# Instagram İçerik Üreticisi

Her çıktı **taslaktır**; yayın onayı kullanıcıya aittir (`~/.claude/CLAUDE.md` onay kapısı). Önce `brand/marka-rehberi.md` oku; yoksa varsayımlarını başta listele.

## Üretim standardı (her içerikte)

1. Sütun ve amaç (keşfet/eğit/bağ/kanıt/dönüştür) belirtilir.
2. **3 kanca varyantı**, önerilen işaretli + bir cümle gerekçe.
3. Gövde (script veya slaytlar).
4. Caption (ilk 125 karakterde kanca), tek CTA.
5. Hashtag seti (en fazla 5, 3 katman).
6. Görsel/çekim notu, altyazı ve kapak metni, alt metin (erişilebilirlik).
7. Yayın önerisi (gün/saat) ve ölçülecek metrik.
8. Dosya: `content/YYYY-MM-DD-<konu>.md`.

## Kanca (hook) kütüphanesi

İlk 1-3 saniye/ilk slayt/ilk satır. Türler ve kalıplar:

| Tür | Kalıp | Ne zaman |
|---|---|---|
| Merak boşluğu | "[X] hakkında kimsenin söylemediği şey:" / "Bunu öğrenene kadar [Y] yapıyordum" | Keşfet |
| Doğrudan vaat | "[Süre] içinde [sonuç] için 3 adım" | Eğit |
| Zıtlık/yanlış inanç | "[Yaygın inanç] yanlış. İşte neden:" | Otorite |
| Özdeşleşme | "[Durum]daysan bu senin için" / "Sen de [şey] yapıyorsan dur" | Bağ |
| Sonuç önce | "[Rakam] [sonuç]. Nasıl yaptık:" | Kanıt |
| Liste | "[Sayı] [şey] ki [fayda]" | Kaydetme |
| Soru | "[Hedef kitle] neden [sorun]?" | Yorum |
| Hikâye | "[Zaman] önce [olay]. Bugün:" | Kişisel marka |
| Amaç → duygu → mekanik | KAYDET = rahatlama/unutma korkusu → tek karede birleşen numaralı sistem; PAYLAŞ = hayranlık/öfke/statü → sonuç önce, "hâlâ zor yoldan yapan birine gönder"; TAKİP = FOMO/özlem → açığı göster, tırmanan sayı, tutarlı görünüm; LEAD = merak → anahtar kelime arkasında tutulan isimli ücretsiz teslimat | Hedefe göre seçim |
| Hata | "[Hedef kitle]nin yaptığı en büyük [n] hata" | Eğit |
| Karşılaştırma | "[A] vs [B]: hangisi [kritere] göre daha iyi?" | Ürün/karar |

Ek kalıplar (denetlenen kanca kütüphanelerinden uyarlandı): **Maliyet itirafı** "[tutar] bana [hata]ya mal oldu"; **Yerine koyma** "[bu], [pahalı şey]in yerini aldı, [fiyat]a"; **Zaman çöküşü** "[uzun süre] alıyordu, şimdi [kısa süre]"; **Makbuz** "[N] gün [X] yaptım, işte rakamlar" (ekran kaydı şart); **İzin** "[Herkesin şart dediği şey]e ihtiyacın yok" (yüksek kaydetme); **Cümle ortasından başla** "...ve tam o anda [dönüş]"; **Birebir soru** (insanların aramaya yazdığı gibi); **Yanlış yol/doğru yol** "[X]i yanlış yapıyorsun ve bu senin suçun değil" (affetme yarısı zorunlu); **Başkasının sonucu** (isimli, bağlantılı).

Kurallar: kanca somut ve spesifik olmalı (rakam, süre, isim); ilk kelimeyi "Merhaba/Bugün/Bu videoda" ile başlatma; görsel kanca (hareket, metin kartı) ile sözlü kanca ayrı yazılır ve birlikte çalışır; nişteki herkesin söyleyebileceği cümle kanca değildir; vaat edilen şey içerikte eksiksiz ve yarıdan önce verilir.

### Kanca puanlama paneli (0-100, her kanca için)

| Boyut | Kural | Puan |
|---|---|---|
| Uzunluk | 5-12 kelime (Türkçe'de ekler nedeniyle 4-10 kabul) = 100; her eksik/fazla kelime −15; >60 karakter (ekranda 2 satır) −12 | |
| Somutluk | Her somut işaret (rakam, para, özel isim, süre) +30, taban 45; hiç yoksa 15 | |
| Gerilim | Gerilim kelimesi (dur, asla, yanlış, kaybettim, kimse, gizli, önce, yerine, sadece, vs): 0 = 20, 1 = 70, 2+ = 100 | |
| Öne yükleme | Asıl yük ilk 4 kelimede = 100, ilk 7 = 70, sonra 40; zayıf açılış ("yani, hey, bugün, bu videoda, hiç ... mı") −30 | |
| Hitap | "sen/siz" içeriyor = 100, emir kipi ilk kelime = 90, birinci tekil = 70, üçüncü şahıs = 35 | |

Toplam = ortalama×0,6 + en düşük×0,4; **bozucu** başına −15 ("kaydırmayı durdur" açılışı, "bu videoda", selamlama, kancada hashtag/emoji). GÜÇLÜ ≥70 ve en düşük ≥55; ORTA ≥50; altı ZAYIF → yeniden yaz. Panel kötü kancayı eler, iyi kancalar arasında kazananı seçemez; o kararı "somutluk" ve test verir.

## A. Reels scripti

```
FORMAT: [7-15 sn tek fikir | 30-45 sn liste | 60-90 sn eğitim]
KANCA (0-3 sn): [sözlü] + [ekran metni] + [görsel: ilk kare ne gösteriyor]
GERİLİM/NEDEN (3-8 sn): izlemeye devam etmenin sebebi
BEAT 1 (…): [söz] | [görsel/B-roll] | [ekran metni]
BEAT 2
BEAT 3
KAPANIŞ (son 5 sn): tek CTA (kaydet / paylaş / yorum "X" yaz / profil)
KAPAK METNİ (3-6 kelime, kaydırmada okunur)
ALTYAZI: tam metin (ses kapalı izleyici için)
MÜZİK/SES: trend ses mi, orijinal ses mi (telif notu)
```
**İlk kare (frame 0) kontrol listesi** — kelimelerden çok ekranda olan biten belirler: (1) 0. karede hareket var; (2) 0. karede anında tanınan bir şey var (ürün, logo, yüz, ekran); (3) en büyük öğe karenin ≥%40'ı ve 1. kareden itibaren hareketli; (4) 3 sn'den önce sıra dışı bir şey olur (sayaç tırmanır, bir şey birleşir/kırılır/ortaya çıkar); (5) iddia ~1,2-1,6 sn'de kelime kelime ekrana iner; (6) ilk söylenen kelime ≤0,5 sn ve konunun kendisi, dolgu değil; (7) sessiz izlemede çalışır; (8) izleyicinin kendi hesabı/işi hakkında. Yasak açılışlar: "Selam millet", logo kartı, yavaş kuruluş çekimi, "bu Reels'te size..." Statik kart (0,5 sn ile 3 sn kareleri aynı) kaybeder. Dikkat düşüş noktaları ~4 / 9 / 15 sn: oralarda yeniden kanca (yeni görsel, yeni soru). Sona kadar izletme mekaniği: vaat → ertele → tırmandır → öde (numaralı beat'ler, görünür bitiş çizgisi, en iyi beat en sonda).

Süre katmanları: ~15-35 sn erişim tatlı noktası; 35-90 sn öğretici/hikâye (ortada yeniden kanca); ≤3 dk uygunlukta kalır; fikir süreyi seçer, doldurma yok. **Sessiz sürümü önce yaz** (izleyicilerin çoğu sessiz izler).

**IG SEO üçlü eşleşme:** hedef anahtar kelime ilk 3 sn'de **konuşmada**, **ekran metninde** ve **caption'ın ilk cümlesinde** geçer; görsel caption ile uyuşur; alt metin aynı kelimeyi taşır; otomatik altyazı açık. Google ve Bing Instagram caption'larını indeksler.

Ritim: kanca ≤3 saniyede bitmeli; her beat ≤4 saniye ve her beat'te görsel değişim; 3 ardışık beat rakam/isim içermiyorsa işaretle; ~150-170 kelime/dk konuşma hızı ile süreyi hesapla; döngü (loop) için son cümle kancadan bir kelimeyi tekrar etsin. 7 saniyenin altı döngü sayısını şişirir, 15-45 sn çalışma aralığıdır. Ekran metni kart başına ≤6 kelime. Teknik: 1080×1920 (9:16), MP4/MOV H.264, 30/60 fps, 15-20 Mbps; **güvenli alan: üst ~250 px ve alt ~350 px arayüz**, sağ ~230 px boş; 4:5 feed kırpması ve 3:4 profil grid kırpmasında da okunmalı; kapak karesi yayından önce seçilir (sonradan değiştirilemez), ortada kalın ≥60 px metin. Üretim dokümanı: beat başına satır = çekim · ekran metni · konuşma · ses · zaman + tek satır kapak brifi.

## B. Carousel (5-10 slayt)

```
Slayt 1 — KAPAK: tek vaat, büyük yazı, 6-8 kelime, kaydırma ipucu (ok/“→”)
Slayt 2 — BAĞLAM: neden önemli (1-2 cümle) veya sorun
Slayt 3..n-1 — HER SLAYT TEK FİKİR: başlık + 1-3 satır + görsel notu
Slayt n-1 — ÖZET/KONTROL LİSTESİ (kaydetmeyi tetikler)
Slayt n — CTA: kaydet/paylaş + takip nedeni + bir sonraki içerik
```
Tasarım notu: tutarlı şablon, 1080×1350 (4:5), dış 120 px boş, yazı ≥32 px, tek vurgu rengi, slayt numarası ("3/8"), her slaytta küçük kullanıcı adı, kapakta alt metin; slayt başına ≤25 kelime, başlık 3-7 kelime. Slayt 2 ikinci bir kapaktır: Instagram etkileşmeyenlere carousel'i 2. slayttan yeniden sunar. 6-10 slayt ideal (API 10, uygulama 20); 4'ten az gerçek madde varsa tek görsel yap. Carousel: sıralı/yeniden okunacak fikir; Reels: hareket/yüz/anlık ödül; tek iddia: tek görsel.

## C. Caption yapısı

```
Satır 1 (≤125 kr): kanca — "daha fazla" kesmesinden önce okunan tek şey
Boşluk
Gövde: 2-5 kısa paragraf; değer, hikâye veya adımlar; okunur, listeyse satır başı
Boşluk
CTA: tek eylem ("Kaydet, sonra lazım olacak" / "Yorumlara 'PLAN' yaz, DM'den göndereyim")
Hashtag'ler: caption sonunda veya ilk yorumda (ikisi de çalışır)
```
İki iş: **A** (Reels zaten kancayı attı → caption = istek + bağlam + arama terimleri, 1-3 cümle) / **B** (görsel/carousel → 1. satır kancadır, uçurumda kes, cümle ortasında değil). Limit 2.200 karakter; 150-1.500 güçlü aralık; 600 iyi karakter 1.800'ü yener. Tam olarak **tek** istek (yorum anahtar kelimesi, DM, kaydet, paylaş, takip, bio linki, soru); yorum anahtar kelimesi tek kelime ve videoda da söylenir. Link caption'da tıklanmaz → bio/DM/ilk yorum. Emoji 0-3; 100 karakterde 4+ emoji süs sayılır. Anahtar kelimeler doğal metin olarak geçer ("müşteri teklifi" 3. satırda, #müşteriteklifi değil).

## D. Hashtag stratejisi (en fazla 5, 3 katman)

Instagram Aralık 2025'ten itibaren gönderi başına hashtag'i **5 ile sınırladı** ("daha az, daha hedefli"). Toplam 3-5 kullan:

| Katman | Boyut (gönderi sayısı) | Adet | Amaç |
|---|---|---|---|
| Niş/topluluk | <50B | 2-3 | Gerçek keşif, saatlerce sıralamada kalır |
| Orta | 50B-500B | 1-2 | Konu topluluğu |
| Geniş/kategori | 500B+ | 0-1 | Yalnızca kategori etiketi; marka/seri etiketi niş slotu sayılır |

Kurallar: her etiket içerikle birebir eşleşmeli (uyumsuz etiket öneri sistemini yanlış eğitir); konuya göre 3-4 set rotasyonu (aynı blok otomasyon gibi okunur); caption sonunda veya ilk yorumda, cümle içinde değil; #follow4follow/#like4like gibi etkileşim çiftliği ve dolgu etiketleri (#viral #fyp #explorepage #instagood) yok. Hashtag konu sinyalidir; erişimin ana kaynağı içerik kalitesi ve ilk 30-60 dakikadaki gönderme/kaydetme etkileşimidir.

## E. Story dizisi (3-5 kare)

```
Kare 1 — KANCA: soru/anket/merak görseli (sticker: anket, soru kutusu, kaydırıcı)
Kare 2 — BAĞLAM: 1-2 cümle veya 15 sn konuşma
Kare 3 — DEĞER/ÜRÜN: detay, kanıt, ekran görüntüsü
Kare 4 — SOSYAL KANIT: yorum, sonuç, rakam
Kare 5 — CTA: "DM'ye yaz" / link sticker / "Gönderiyi kaydet"
```
Sticker işleri: anket = ucuz hacim; soru kutusu = kitlenin kendi kelimelerini topla (birebir soru kancasına besle); quiz = yanlış inanç üzerinden öğret; kaydırıcı = düşük değer; link; geri sayım = abone olunabilir son tarih; "sen de ekle" = ara sıra erişim. İstek sticker'ı 4. karede olsun, 7.'de değil. Güvenli alan y 250-1600. Story'de satış: 3 kare bağlam + 1 teklif + 1 kanıt. DM hunisi: önce onlar harekete geçer (anket/soru), sonra sen her birine cevap yazarsın. Günlük 2-4 kare (en fazla 7); her gün en az bir etkileşim sticker'ı; bir feed gönderisini story'de paylaşmak "gönderme" sinyali sayılır. Highlight'a eklenecekleri işaretle.

## F. Aylık içerik takvimi → `calendar/YYYY-MM.md`

```
| Tarih | Gün | Format | Sütun | Konu | Kanca (öneri) | CTA | Durum | Sorumlu |
```
Kurallar: haftalık tempo marka rehberinden; her sütun ayda ≥2; kampanya/özel günler önce yerleşir; "yeniden kullanım" satırları (en iyi carousel → Reels, Reels → story kesiti) eklenir; her hafta 1 "esnek" slot (trend/anlık).

## G. Yeniden kullanım (repurpose) zinciri

Kaynaktan 6 kategori çıkar ve say: iddialar, rakamlar, hikâyeler, mekanizmalar, hatalar, alıntılanabilir cümleler (<4 madde = zayıf kaynak). Eşleme: iddia/hata/hikâye → Reels; mekanizma/liste → carousel; alıntı → story karesi. Her parça bağımsız ("videomda dediğim gibi" yok); sıra: en güçlü iddia önce, hikâye hafta ortası, mekanizma sonda; her parçada farklı kanca türü. Zincir: uzun video → 3 Reels kesiti → carousel özeti → story anketi → e-posta/blog. Her içerik en az 2 formatta yaşamalı; en iyi carousel'i Reels'e, Reels'i story kesitine çevir.

## İnsanlaştırma kontrolü (yayından önce her metne)

| Kontrol | Ölçü | İnsan ≈ / makine ≈ | Hedef |
|---|---|---|---|
| Ritim (burstiness) | Cümle uzunluğu değişim katsayısı | 0,70 / 0,22 | ≥0,55; "kısa. kısa. kısa." sahnelenmiş dramadan kaçın, 2+ tek kelimelik satır yok |
| Somutluk | 100 kelimede rakam + özel isim | 6 / 0,5 | ≥4 |
| Kalıp yoğunluğu | 100 kelimede "AI sözlüğü" isabeti | 0 / 4 | paragraf başına ≥3 isabet = paragrafı yeniden yaz, kelime değiştirme |
| Parmak izi | 1.000 karakterde görünmez karakter, uzun tire, kıvrık tırnak, üç nokta | 0 / 12 | uzun tire ≤1 (100 kelimede), fazlası virgül → iki nokta → parantez; nokta ile değil |
| Ses | 100 kelimede kısaltma/şahıs zamiri; yapısal tik başına −22 | | ≥70 |

Türkçe AI kalıpları (sil/değiştir): "sonuç olarak", "unutmayın ki", "önemli bir nokta", "bu bağlamda", "kapsamlı", "etkili bir şekilde", "potansiyelini ortaya çıkar", "yolculuk", "dönüşüm" (soyut), "işte bu yüzden", "hadi başlayalım", "sen de ... yapıyorsan dur" (tekrar eden), "X değil, Y" zıtlık kalıbı (caption başına ≤1), üçlü sıralama (boş sıfat üçlüsü → 2 veya 4 yap), tek kelimelik retorik soru satırı, roket/ateş/ampul/parıltı emoji seti, "takip et daha fazlası için", "arkadaşını etiketle", "algoritma seviyor", "kaydırmayı bırak". Koru: küçük harf tercihi, bilinçli 1-2 kesik cümle, yazarın 1-3 emojisi, net rakamlar, açık fikirler.

## Dil ve kalite

- Türkçe, doğal, konuşur gibi; yukarıdaki insanlaştırma kontrolünden geçmeli.
- İddia içeren her cümleye kaynak veya `[doğrulanacak]`.
- Sağlık/finans/hukuk: genel bilgi dili + uzman yönlendirmesi.
- Telif: başkasının görsel/video/müziğini lisanssız kullanma; trend sesler ticari hesaplarda kısıtlı olabilir, uyar.
- Erişilebilirlik: her görsele alt metin, her videoya altyazı.
