-- Yapada Fiyat Gör — D1 şeması
CREATE TABLE IF NOT EXISTS urunler (
  barkod        TEXT PRIMARY KEY,
  stok_kodu     TEXT,
  ad            TEXT NOT NULL,
  marka         TEXT,
  grup          TEXT,
  birim         TEXT,
  kdv_orani     REAL,
  fiyat         REAL,
  para_birimi   TEXT DEFAULT 'TRY',
  stok_miktari  REAL,
  aktif         INTEGER NOT NULL DEFAULT 1,
  resim_url     TEXT,
  sync_id       TEXT,
  guncelleme    TEXT
);
CREATE INDEX IF NOT EXISTS idx_urunler_stok_kodu ON urunler(stok_kodu);
CREATE INDEX IF NOT EXISTS idx_urunler_ad ON urunler(ad);

CREATE TABLE IF NOT EXISTS senkron_log (
  sync_id   TEXT PRIMARY KEY,
  baslangic TEXT,
  bitis     TEXT,
  adet      INTEGER,
  kaynak    TEXT
);

CREATE TABLE IF NOT EXISTS sorgu_log (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  zaman     TEXT,
  barkod    TEXT,
  bulundu   INTEGER
);
