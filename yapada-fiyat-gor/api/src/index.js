/**
 * Yapada Fiyat Gör — Cloudflare Worker API (D1)
 *
 * Uçlar
 *   GET  /api/urun?barkod=8690...     Müşteriye açık. Barkoddan ürün + fiyat + stok durumu.
 *   GET  /api/ara?q=hot wheels        Müşteriye açık. Ada göre en çok 20 sonuç.
 *   GET  /api/durum                   Son senkron zamanı ve aktif ürün sayısı.
 *   POST /api/sync                    Bearer SYNC_TOKEN. {sync_id, urunler:[...]} toplu upsert.
 *   POST /api/sync/bitir              Bearer SYNC_TOKEN. {sync_id} -> bu turda gelmeyenleri pasife al.
 *
 * Statik sayfa (web/) Wrangler [assets] ile aynı Worker'dan sunulur.
 */

const JSON_HEADERS = { "content-type": "application/json; charset=utf-8" };

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const origin = request.headers.get("Origin") || "";
    const cors = corsHeaders(origin, env);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }
    if (!url.pathname.startsWith("/api/")) {
      // Varlıklar (web/) Worker'dan önce sunulur; buraya düşen bilinmeyen yol 404.
      return json({ hata: "bulunamadi" }, 404, cors);
    }

    try {
      if (request.method === "GET" && url.pathname === "/api/urun") {
        return await urunGetir(url, env, ctx, cors);
      }
      if (request.method === "GET" && url.pathname === "/api/ara") {
        return await ara(url, env, cors);
      }
      if (request.method === "GET" && url.pathname === "/api/durum") {
        return await durum(env, cors);
      }
      if (request.method === "POST" && url.pathname === "/api/sync") {
        if (!yetkili(request, env)) return json({ hata: "yetkisiz" }, 401, cors);
        return await senkronYaz(request, env, cors);
      }
      if (request.method === "POST" && url.pathname === "/api/sync/bitir") {
        if (!yetkili(request, env)) return json({ hata: "yetkisiz" }, 401, cors);
        return await senkronBitir(request, env, cors);
      }
      return json({ hata: "bulunamadi" }, 404, cors);
    } catch (err) {
      console.error(err && err.stack ? err.stack : err);
      return json({ hata: "sunucu", mesaj: String(err && err.message ? err.message : err) }, 500, cors);
    }
  },
};

// ---------------------------------------------------------------------------
// Yardımcılar
// ---------------------------------------------------------------------------

function json(veri, status = 200, ekBaslik = {}) {
  return new Response(JSON.stringify(veri), { status, headers: { ...JSON_HEADERS, ...ekBaslik } });
}

function corsHeaders(origin, env) {
  const izinli = String(env.ALLOWED_ORIGINS || "")
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
  const h = { Vary: "Origin" };
  if (origin && izinli.includes(origin)) {
    h["Access-Control-Allow-Origin"] = origin;
    h["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS";
    h["Access-Control-Allow-Headers"] = "Content-Type, Authorization";
    h["Access-Control-Max-Age"] = "86400";
  }
  return h;
}

function yetkili(request, env) {
  const beklenen = env.SYNC_TOKEN;
  if (!beklenen) return false;
  const auth = request.headers.get("Authorization") || "";
  const token = auth.startsWith("Bearer ") ? auth.slice(7).trim() : "";
  return token.length > 0 && sabitZamanEsit(token, beklenen);
}

function sabitZamanEsit(a, b) {
  if (a.length !== b.length) return false;
  let fark = 0;
  for (let i = 0; i < a.length; i++) fark |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return fark === 0;
}

function barkodTemizle(b) {
  return String(b || "").replace(/[^0-9A-Za-z]/g, "");
}

/** Okuyucular UPC-A'yı 12 hane, EAN-13'ü 13 hane verir; kayıt tersi olabilir. Adayları sırala. */
function barkodAdaylari(b) {
  const adaylar = [b];
  if (/^\d+$/.test(b)) {
    if (b.length === 12) adaylar.push("0" + b);
    if (b.length === 13 && b.startsWith("0")) adaylar.push(b.slice(1));
    const sifirsiz = b.replace(/^0+/, "");
    if (sifirsiz && sifirsiz !== b && !adaylar.includes(sifirsiz)) adaylar.push(sifirsiz);
  }
  return adaylar;
}

function stokDurumu(miktar, esik) {
  if (miktar === null || miktar === undefined) return null;
  const m = Number(miktar);
  if (!(m > 0)) return { kod: "tukendi", metin: "Tükendi" };
  if (m <= esik) return { kod: "az", metin: m === 1 ? "Son 1 adet" : `Son ${Math.floor(m)} adet` };
  return { kod: "var", metin: "Stokta" };
}

function urunCikti(satir, env) {
  const esik = Number(env.AZ_STOK_ESIGI || 3);
  return {
    barkod: satir.barkod,
    stok_kodu: satir.stok_kodu,
    ad: satir.ad,
    marka: satir.marka || "",
    grup: satir.grup || "",
    birim: satir.birim || "",
    kdv_orani: satir.kdv_orani,
    fiyat: satir.fiyat,
    para_birimi: satir.para_birimi || "TRY",
    stok: stokDurumu(satir.stok_miktari, esik),
    resim_url: satir.resim_url || null,
    guncelleme: satir.guncelleme,
  };
}

// ---------------------------------------------------------------------------
// Müşteriye açık uçlar
// ---------------------------------------------------------------------------

async function urunGetir(url, env, ctx, cors) {
  const barkod = barkodTemizle(url.searchParams.get("barkod"));
  if (barkod.length < 4 || barkod.length > 32) {
    return json({ hata: "gecersiz_barkod" }, 400, cors);
  }
  const adaylar = barkodAdaylari(barkod);
  const yerler = adaylar.map(() => "?").join(",");
  const satir = await env.DB.prepare(
    `SELECT * FROM urunler WHERE aktif = 1 AND barkod IN (${yerler}) LIMIT 1`
  )
    .bind(...adaylar)
    .first();

  ctx.waitUntil(
    env.DB.prepare("INSERT INTO sorgu_log (zaman, barkod, bulundu) VALUES (?, ?, ?)")
      .bind(new Date().toISOString(), barkod, satir ? 1 : 0)
      .run()
      .catch(() => {})
  );

  if (!satir) {
    return json({ bulunamadi: true, barkod }, 404, { ...cors, "Cache-Control": "no-store" });
  }
  return json(urunCikti(satir, env), 200, { ...cors, "Cache-Control": "public, max-age=60" });
}

async function ara(url, env, cors) {
  const q = String(url.searchParams.get("q") || "").trim();
  if (q.length < 2) return json({ sonuclar: [] }, 200, cors);
  const desen = "%" + q.replace(/[%_]/g, " ") + "%";
  const { results } = await env.DB.prepare(
    `SELECT * FROM urunler WHERE aktif = 1 AND (ad LIKE ? OR marka LIKE ? OR stok_kodu LIKE ?)
     ORDER BY ad LIMIT 20`
  )
    .bind(desen, desen, desen)
    .all();
  return json({ sonuclar: results.map((r) => urunCikti(r, env)) }, 200, {
    ...cors,
    "Cache-Control": "public, max-age=60",
  });
}

async function durum(env, cors) {
  const son = await env.DB.prepare(
    "SELECT sync_id, bitis, adet FROM senkron_log WHERE bitis IS NOT NULL ORDER BY bitis DESC LIMIT 1"
  ).first();
  const sayi = await env.DB.prepare("SELECT COUNT(*) AS n FROM urunler WHERE aktif = 1").first();
  return json(
    { son_senkron: son ? son.bitis : null, son_sync_id: son ? son.sync_id : null, aktif_urun: sayi ? sayi.n : 0 },
    200,
    { ...cors, "Cache-Control": "no-store" }
  );
}

// ---------------------------------------------------------------------------
// Senkron uçları (Wolvox tarafındaki servis çağırır)
// ---------------------------------------------------------------------------

const UPSERT_SQL = `
INSERT INTO urunler (barkod, stok_kodu, ad, marka, grup, birim, kdv_orani, fiyat, para_birimi,
                     stok_miktari, aktif, resim_url, sync_id, guncelleme)
VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, 1, ?11, ?12, ?13)
ON CONFLICT(barkod) DO UPDATE SET
  stok_kodu = excluded.stok_kodu,
  ad = excluded.ad,
  marka = excluded.marka,
  grup = excluded.grup,
  birim = excluded.birim,
  kdv_orani = excluded.kdv_orani,
  fiyat = excluded.fiyat,
  para_birimi = excluded.para_birimi,
  stok_miktari = excluded.stok_miktari,
  aktif = 1,
  resim_url = COALESCE(excluded.resim_url, urunler.resim_url),
  sync_id = excluded.sync_id,
  guncelleme = excluded.guncelleme`;

async function senkronYaz(request, env, cors) {
  let govde;
  try {
    govde = await request.json();
  } catch {
    return json({ hata: "gecersiz_json" }, 400, cors);
  }
  const syncId = String(govde.sync_id || "").slice(0, 64);
  const urunler = Array.isArray(govde.urunler) ? govde.urunler : [];
  if (!syncId || urunler.length === 0) return json({ hata: "eksik_veri" }, 400, cors);
  if (urunler.length > 1000) return json({ hata: "paket_cok_buyuk", azami: 1000 }, 413, cors);

  const simdi = new Date().toISOString();
  await env.DB.prepare(
    "INSERT INTO senkron_log (sync_id, baslangic, kaynak) VALUES (?, ?, ?) ON CONFLICT(sync_id) DO NOTHING"
  )
    .bind(syncId, simdi, String(govde.kaynak || "wolvox-sdk").slice(0, 32))
    .run();

  const stmt = env.DB.prepare(UPSERT_SQL);
  const toplu = [];
  let atlanan = 0;
  for (const u of urunler) {
    const barkod = barkodTemizle(u.barkod);
    const ad = String(u.ad || "").trim();
    if (!barkod || !ad) {
      atlanan++;
      continue;
    }
    toplu.push(
      stmt.bind(
        barkod,
        String(u.stok_kodu || ""),
        ad.slice(0, 300),
        String(u.marka || "").slice(0, 100),
        String(u.grup || "").slice(0, 100),
        String(u.birim || "").slice(0, 20),
        sayiVeyaNull(u.kdv_orani),
        sayiVeyaNull(u.fiyat),
        String(u.para_birimi || "TRY").slice(0, 8),
        sayiVeyaNull(u.stok_miktari),
        u.resim_url ? String(u.resim_url).slice(0, 500) : null,
        syncId,
        simdi
      )
    );
  }
  // D1 batch tek işlemde çalışır; 100'erli parçalara bölmek bağlı-değişken sınırına takılmayı önler.
  let yazilan = 0;
  for (let i = 0; i < toplu.length; i += 100) {
    const parca = toplu.slice(i, i + 100);
    await env.DB.batch(parca);
    yazilan += parca.length;
  }
  return json({ sync_id: syncId, yazilan, atlanan }, 200, cors);
}

async function senkronBitir(request, env, cors) {
  let govde;
  try {
    govde = await request.json();
  } catch {
    return json({ hata: "gecersiz_json" }, 400, cors);
  }
  const syncId = String(govde.sync_id || "").slice(0, 64);
  if (!syncId) return json({ hata: "eksik_veri" }, 400, cors);
  const simdi = new Date().toISOString();

  const pasif = await env.DB.prepare(
    "UPDATE urunler SET aktif = 0 WHERE aktif = 1 AND (sync_id IS NULL OR sync_id <> ?)"
  )
    .bind(syncId)
    .run();
  const aktif = await env.DB.prepare("SELECT COUNT(*) AS n FROM urunler WHERE aktif = 1").first();
  await env.DB.prepare(
    "INSERT INTO senkron_log (sync_id, baslangic, bitis, adet, kaynak) VALUES (?1, ?2, ?2, ?3, ?4) " +
      "ON CONFLICT(sync_id) DO UPDATE SET bitis = ?2, adet = ?3"
  )
    .bind(syncId, simdi, Number(govde.adet || (aktif ? aktif.n : 0)), String(govde.kaynak || "wolvox-sdk").slice(0, 32))
    .run();

  return json(
    { sync_id: syncId, aktif: aktif ? aktif.n : 0, pasife_alinan: pasif.meta ? pasif.meta.changes : null },
    200,
    cors
  );
}

function sayiVeyaNull(v) {
  if (v === null || v === undefined || v === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
}
