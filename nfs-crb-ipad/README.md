# NFS Carbon Browser Edition (nfscrb.xyz) — iPad uyumluluk yaması

Bu klasör, [metinjakupi/nfs-crb](https://github.com/metinjakupi/nfs-crb) deposuna
(2026-11-07, commit `1cdd6b7`) karşı hazırlanmış bir iPad uyumluluk yaması içerir.
Üst depoya yazma yetkisi bu oturumda yoktu; bu yüzden değişiklik `ipad-support.diff`
olarak burada tutulur ve üst depoya bir fork + pull request ile taşınır.

## Durum tespiti

Oyun, Need for Speed: Carbon'un WebAssembly + WebGPU'ya statik yeniden derlemesidir.
Orijinal oyun dosyaları depoda yoktur; oyuncu kendi Carbon 1.4 kurulumunu tarayıcıya
içe aktarır. Depo iPhone için dokunmatik kontroller, düşük bellek profili ve Safari 26
WebGPU denetimi içeriyor; ancak iPad'e özgü üç boşluk vardı:

1. **Yatay yönlendirme beklemesi yalnızca telefonlar içindi.** `player/index.html` ve
   `touch.js`, ekranın kısa kenarı 600 px'ten küçük cihazlarda yatay moda dönülmesini
   bekliyordu. iPad bu eşiğin üstünde kaldığı için dikey tutulan iPad'de oyun dikey
   çözünürlükle başlıyor ve oturum boyunca öyle kalıyordu (oyun pencere boyutunu
   yalnızca açılışta okur).
2. **Trackpad veya Magic Keyboard bağlı iPad masaüstü sanılıyordu.** iPadOS Safari
   varsayılan olarak masaüstü sitesini ister (user agent "Macintosh") ve bir işaretleme
   aygıtı bağlıyken `(pointer: coarse)` sorgusu eşleşmez. Bu durumda telefonlar için
   yazılmış çözünürlük sınırı (`start.js`), küçük içe aktarma arabellekleri
   (`custom-install.js`) ve klasör seçici gizleme (`saves.js`) devreye girmiyordu.
   Sonuç: tam Retina çözünürlükte render ve daha yüksek bellek kullanımı; bu da iPad'de
   sekmenin kapanmasına yol açabilir.
3. **Belgeler iPad'den hiç söz etmiyordu.** SSS ve README "yalnızca masaüstü Chrome/Edge"
   diyordu; iPadOS 26 + Safari gereksinimi, normal sekme (gizli sekme değil) ve dosya
   içe aktarma yolu hiçbir yerde yazmıyordu.

## Yamanın yaptığı değişiklikler

| Dosya | Değişiklik |
| --- | --- |
| `source/kit/web/player/index.html` | `iPadOS()` yardımcı işlevi; yatay bekleme artık tüm telefon ve tabletler için, iPad'e özel mesajla |
| `source/web/start.js` | `isTouchDevice()` iPad'i işaretçi türünden bağımsız tanır; çözünürlük sınırı iPad'de her zaman uygulanır |
| `source/web/touch.js` | "Döndür" uyarısı tabletlerde de görünür; metin "Rotate your iPad to landscape" |
| `source/web/custom-install.js` | `phone()` iPad'i kapsar; 4 MiB bellek içi özet sınırı iPad'de de geçerli |
| `source/web/saves.js` | Klasör seçici düğmesi iPad'de gizlenir (Safari'de `showDirectoryPicker` yok) |
| `tools/site/faq.html` | "What do I need to play?" güncellendi; "Can I play on an iPad?" sorusu eklendi (hem görünür metin hem JSON-LD) |
| `README.md`, `CHANGELOG.md` | iPad/iPhone yolu ve değişiklik kayıtları |

iPad tespiti her yerde aynı ifadedir:

```js
/iPad/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1)
```

## Doğrulanan ve doğrulanamayan kısımlar

- Düzenlenen dört betik ve oyuncu sayfasının satır içi betiği `node --check` ile
  ayrıştırıldı; sözdizimi hatası yok.
- `tools/carbon-mobile-beta.py`'nin `index.html` içinde aradığı çapa dizgileri
  (`startupPhase = phase;`, `if (canonicalRedirect) return;`, `gameRunning = true;`)
  değişmeden duruyor.
- **Gerçek iPad'de test edilmedi.** Bu ortamda oyun dosyaları, Emscripten derleme zinciri
  ve bir iPad yok; nfscrb.xyz sitesi de bu ortamın ağ politikası dışında kaldığı için
  canlı sürüm incelenemedi. Yama yalnızca tarayıcı katmanındaki JavaScript/HTML'i
  değiştirir, WebAssembly derlemesi gerektirmez.

## Yamayı üst depoya taşıma

```sh
git clone https://github.com/<kendi-hesabın>/nfs-crb   # önce GitHub'da fork oluştur
cd nfs-crb
git checkout -b ipad-support
git apply /yol/nfs-crb-ipad/ipad-support.diff
git commit -am "Treat iPad like a phone and wait for landscape on tablets"
git push -u origin ipad-support
```

Ardından `metinjakupi/nfs-crb` deposuna pull request aç. Yama `1cdd6b7`'ye göre
hazırlandı; üst depo ilerlediyse `git apply --3way` dene.

## iPad'de oynamadan önce kontrol listesi

Yama yayına alınsa bile şu koşullar sağlanmadan oyun iPad'de açılmaz:

1. **iPadOS 26 veya üstü.** WebGPU Safari 26 ile geldi; eski sürümlerde oyun
   "This iPhone or iPad does not provide the WebGPU support" hatası verir.
2. **Safari'nin kendisi, normal sekme.** Uygulama içi tarayıcılar (Instagram, Discord
   vb.) ve Gizli Sekme çalışmaz: ilki çapraz kaynak yalıtımı ve WebGPU vermez,
   ikincisi oyun dosyalarının saklandığı depolamayı reddeder.
3. **Yatay tutuş.** Oyun yatay moda dönülmesini bekler.
4. **Kendi Carbon 1.4 dosyaların.** Oyun dosyaları siteden gelmez; Dosyalar
   uygulamasından **Manage game files** ile içe aktarılır. iPad'de klasör seçici yoktur,
   dosyalar seçilerek yüklenir.
5. **Bellek.** Oyun 2 GB'lık bir WebAssembly alanı ayırır. 3 GB RAM'li eski iPad'lerde
   sekme yüklenirken kapanabilir; diğer sekmeleri ve uygulamaları kapat.
6. Sorun sürerse sitedeki `mobile-check.html` sayfası (depoda `tools/site/`) WebGPU,
   paylaşımlı bellek ve depolama denetimlerini tek tek raporlar; çıktısını oyun içindeki
   **Send report** ile gönderebilirsin.
