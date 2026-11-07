# Yapada Fiyat Gör

Müşterinin telefonuyla sitenizden ürün barkodunu okutup güncel fiyatı ve stok durumunu gördüğü uygulama.
Veri kaynağı AKINSOFT Wolvox ERP; bağlantı resmî **Wolvox SDK** (Kontrol Paneli, port 3056) üzerinden,
veritabanına doğrudan dokunmadan kurulur.

```
Wolvox PC                              Cloudflare (ücretsiz katman yeter)          Müşteri telefonu
┌───────────────────────┐   HTTPS      ┌──────────────────────────────┐   HTTPS   ┌──────────────────┐
│ Kontrol Paneli (SDK)  │◄─── yerel ───│                              │◄──────────│ fiyat.yapada...  │
│ sync/wolvox_sync.py   │────────────► │ Worker  /api/urun /api/sync  │           │ kamera + barkod  │
│ (10 dk'da bir)        │  Bearer tok. │ D1      urunler tablosu      │──────────►│ fiyat kartı      │
└───────────────────────┘              │ Assets  web/index.html       │           └──────────────────┘
                                       └──────────────────────────────┘
```

Mağaza ağına dışarıdan hiçbir bağlantı açılmaz: senkron servisi içeriden dışarıya konuşur.
SDK'nın şifresiz HTTP'si yalnızca Wolvox bilgisayarının içinde kalır.

## Klasörler

| Klasör | İçerik |
|---|---|
| `sync/wolvox_sync.py` | Wolvox SDK'dan stok, fiyat ve miktar çekip API'ye gönderen servis. Yalnızca Python standart kütüphanesi. |
| `sync/mock_sdk_server.py` | Test için sahte SDK (gerçek SDK gibi Base64 konuşur). |
| `api/` | Cloudflare Worker + D1 veritabanı. Müşteri sayfasını da aynı Worker sunar. |
| `web/index.html` | Müşteriye açık sayfa: kamera ile barkod okuma, elle giriş, fiyat kartı, son baktıkları. |

## Ön koşullar

1. **AKINSOFT SDK lisansı.** Bilgi Bankası A257/A3994: "SDK sistemini kullanmaya başlamadan önce Lisans
   departmanı ile görüşerek SDK lisansı açılmasını talep etmeniz gerekmektedir." Size bir **geliştirici kodu**
   (devCode) ve **parolası** (devPass) verilir. AKINSOFT SDK için teknik destek vermez.
2. Wolvox Kontrol Paneli'nin çalıştığı bilgisayarda **Python 3.9+** (python.org kurulumu yeterli).
3. Ücretsiz bir **Cloudflare** hesabı ve bilgisayarınızda Node.js 18+ (yalnızca ilk kurulum için).
4. Sitenizde kameranın açılması için sayfa **https** üzerinden sunulmalı (Cloudflare bunu kendiliğinden sağlar).

## Kurulum

### 1. Bulut tarafı (bir kez)

```bash
cd api
npm install
npx wrangler login
npx wrangler d1 create yapada-fiyat-gor        # çıktıdaki database_id'yi wrangler.toml'a yazın
npx wrangler d1 execute yapada-fiyat-gor --remote --file schema.sql
npx wrangler secret put SYNC_TOKEN             # uzun, rastgele bir anahtar girin (senkron servisi bunu kullanır)
npx wrangler deploy
```

Deploy çıktısındaki adres (`https://yapada-fiyat-gor.<hesap>.workers.dev`) hem sayfadır hem API'dir.
Kendi alan adınızı bağlamak için Cloudflare panelinde Worker'a `fiyat.yapadadukkan.com` gibi bir
"Custom Domain" ekleyin.

### 2. Wolvox tarafı

```bash
cd sync
copy config.example.json config.json       # Windows
```

`config.json` içinde doldurun: Wolvox kullanıcı adı ve parolası, `dev_code` / `dev_pass`, `sirket_kodu`,
`calisma_yili`, API adresi ve `SYNC_TOKEN` ile aynı `token`.

Sırasıyla deneyin:

```bash
python wolvox_sync.py --config config.json --sirketler   # şirket kodu ve çalışma yılını görün
python wolvox_sync.py --config config.json --kesfet      # SDK'nın döndürdüğü alan adlarını görün
python wolvox_sync.py --config config.json --dry-run     # API'ye göndermeden urunler.json üretin, kontrol edin
python wolvox_sync.py --config config.json               # gerçek senkron
```

`--kesfet` çıktısında fiyat ya da miktar alanı beklediğiniz adla gelmiyorsa `config.json`'a
`fiyat_alan_adaylari` / `miktar_alan_adaylari` listelerini ekleyip doğru alan adını başa yazın.
Satış fiyatı Wolvox'ta KDV hariç tutuluyorsa `"fiyat_kdv_dahil": false` yapın; servis KDV'yi ekler.

**Sürekli çalıştırma:** Windows Görev Zamanlayıcı'da "oturum açılışında" tetiklenen bir görev:

```
python C:\yapada\sync\wolvox_sync.py --config C:\yapada\sync\config.json --dongu 600
```

600 saniye = 10 dakikada bir tam senkron. 12-13 bin ürün için SDK çağrısı ve gönderim genelde bir dakikanın altında sürer.

### 3. Siteye yerleştirme

- En basit yol: sitenizdeki "Fiyat Gör" menüsü `https://fiyat.yapadadukkan.com` adresine gitsin.
- Belirli bir barkodla açmak için `?barkod=8690...` eklenebilir (QR kodlu raf etiketleri için kullanışlı).
- Sayfa başka bir alan adından `fetch` ile çağrılacaksa `wrangler.toml` içindeki `ALLOWED_ORIGINS`'e o adresi ekleyin.
- Ürün görseli için `config.json` → `resim_url_sablonu` alanına `{barkod}` veya `{stok_kodu}` içeren bir adres kalıbı yazabilirsiniz.

## API

| Uç | Açıklama |
|---|---|
| `GET /api/urun?barkod=…` | Müşteriye açık. Ürün, KDV dahil fiyat, stok çipi (`var` / `az` / `tukendi`). 12 haneli UPC ile 13 haneli EAN arasındaki baştaki sıfır farkını kendisi dener. |
| `GET /api/ara?q=…` | Ada, markaya veya stok koduna göre en çok 20 sonuç. |
| `GET /api/durum` | Son senkron zamanı ve aktif ürün sayısı. |
| `POST /api/sync` | `Authorization: Bearer SYNC_TOKEN`. `{sync_id, urunler:[…]}` toplu ekle/güncelle. Paket başına en çok 1000. |
| `POST /api/sync/bitir` | Aynı yetki. Bu turda gelmeyen ürünleri pasife alır; sayfada görünmez olurlar. |

Müşteriye stok adedi değil durum gösterilir: eşiğin (`AZ_STOK_ESIGI`, varsayılan 3) altındaysa "Son N adet", yoksa "Stokta" ya da "Tükendi".

## Yerelde deneme

```bash
# 1. terminal: sahte SDK
python sync/mock_sdk_server.py --port 3056
# 2. terminal: yerel API + sayfa
cd api && printf 'SYNC_TOKEN=test\n' > .dev.vars && npx wrangler d1 execute yapada-fiyat-gor --local --file schema.sql && npx wrangler dev --local
# 3. terminal: senkron (config.json'da api.url = http://127.0.0.1:8787, token = test, dev_code/dev_pass = DEMO)
python sync/wolvox_sync.py --config sync/config.json
```

Sonra tarayıcıda `http://localhost:8787/?barkod=887961953404`.

## Bilinen sınırlar

- SDK yalnızca sizin sorduğunuzda cevap verir; fiyat değişikliği siteye en geç bir senkron aralığı sonra yansır.
- SDK'da sayfalama yok; her turda tam liste çekilir. Bu, mevcut ürün sayısında sorun değildir.
- Görseller SDK'dan gelmez; görsel kalıbı ya da e-ticaret görsel adresleri ayrıca eşlenir.
- Kamera yalnızca https ve kullanıcı izniyle açılır; izin yoksa elle giriş çalışır.
