#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yapada Fiyat Gör — Wolvox SDK senkron servisi

Wolvox Kontrol Paneli'ne gömülü SDK (HTTP, port 3056) üzerinden stok kartlarını,
satış fiyatlarını ve miktarları çeker; buluttaki Fiyat Gör API'sine gönderir.

Yalnızca Python standart kütüphanesi kullanır; Windows'ta Python 3.9+ ile çalışır.

Kullanım:
  python wolvox_sync.py --config config.json            # tek sefer senkron
  python wolvox_sync.py --config config.json --dongu 600 # 10 dakikada bir
  python wolvox_sync.py --config config.json --sirketler # şirket/yıl listesi
  python wolvox_sync.py --config config.json --kesfet    # ilk kaydın alan adlarını göster
  python wolvox_sync.py --config config.json --dry-run   # API'ye göndermeden urunler.json yaz

SDK kuralları (AKINSOFT Wolvox SDK Doküman v1.02.01):
  - İstek parametreleri Base64 ile kodlanıp getdata.html? sonrasına eklenir.
  - Yanıtın tamamı Base64 kodludur.
  - wlogin: parola MD5, devCode/devPass AKINSOFT'un verdiği çözüm ortağı bilgileri.
  - Sonraki her istekte tpwd (geçici parola) gönderilir.
"""

import argparse
import base64
import datetime as dt
import hashlib
import json
import logging
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET

LOG = logging.getLogger("wolvox_sync")

VARSAYILAN_CONFIG = {
    "wolvox": {
        "host": "127.0.0.1",
        "port": 3056,
        "kullanici": "SYSDBA",
        "parola": "",
        "dev_code": "",
        "dev_pass": "",
        "sirket_kodu": "",
        "calisma_yili": "",
        "sube_kodu": "",
        "timeout_dk": 60,
        "istek_zaman_asimi_sn": 300,
        "stok_ek_sart": " AND STOK.AKTIF=1",
        "stok_field_list": "",
        "fiyat_no": 1,
        "fiyat_kdv_dahil": True,
        "fiyat_alan_adaylari": [
            "SATIS_FIYATI1", "SATIS_FIYATI_1", "SATIS_FIYAT1", "SATISFIYATI1",
            "FIYATI", "KPB_FIYATI", "SATIS_FIYATI"
        ],
        "miktar_alan_adaylari": [
            "KALAN_MIKTAR", "KALAN_MIKTARI", "MEVCUT_MIKTAR", "MIKTAR", "MIKTARI",
            "KALAN", "BAKIYE", "ENVANTER", "STOK_MIKTARI"
        ],
        "envanter_cek": True,
        "envanter_hesabi": 1,
        "envanter_maliyet_tipi": 5
    },
    "api": {
        "url": "https://fiyat.yapadadukkan.com",
        "token": "",
        "paket_boyutu": 500,
        "resim_url_sablonu": ""
    }
}


# ----------------------------------------------------------------------------
# Yardımcılar
# ----------------------------------------------------------------------------

def derin_birlestir(varsayilan, gelen):
    sonuc = dict(varsayilan)
    for k, v in (gelen or {}).items():
        if isinstance(v, dict) and isinstance(sonuc.get(k), dict):
            sonuc[k] = derin_birlestir(sonuc[k], v)
        else:
            sonuc[k] = v
    return sonuc


def ondalik(deger):
    """Wolvox'un '1.234,56' veya '5,00' biçimindeki sayılarını float'a çevirir."""
    if deger is None:
        return None
    s = str(deger).strip()
    if not s:
        return None
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def barkod_temizle(b):
    if b is None:
        return ""
    return "".join(ch for ch in str(b).strip() if ch.isalnum())


def ilk_dolu(sozluk, anahtarlar):
    for a in anahtarlar:
        if a in sozluk and str(sozluk[a]).strip() != "":
            return sozluk[a]
    return None


# ----------------------------------------------------------------------------
# SDK istemcisi
# ----------------------------------------------------------------------------

class WolvoxSDK:
    def __init__(self, cfg):
        self.cfg = cfg
        self.base = "http://%s:%s/getdata.html?" % (cfg["host"], cfg["port"])
        self.tpwd = None
        self.zaman_asimi = int(cfg.get("istek_zaman_asimi_sn", 300))

    # --- düşük seviye -------------------------------------------------------
    def _istek(self, params):
        sorgu = urllib.parse.urlencode(params, safe="", quote_via=urllib.parse.quote)
        # SDK, parametre dizisinin tamamının Base64 ile kodlanmasını ister.
        # urlencode'un ürettiği %XX kaçışları SDK tarafında çözülmüyor olabilir;
        # bu yüzden değerleri olduğu gibi birleştiriyoruz.
        sorgu = "&".join("%s=%s" % (k, v) for k, v in params.items())
        kodlu = base64.b64encode(sorgu.encode("utf-8")).decode("ascii")
        url = self.base + kodlu
        LOG.debug("SDK GET %s", {k: (v if k not in ("password", "devPass") else "***") for k, v in params.items()})
        req = urllib.request.Request(url, headers={"User-Agent": "YapadaFiyatGorSync/1.0"})
        with urllib.request.urlopen(req, timeout=self.zaman_asimi) as yanit:
            ham = yanit.read()
        try:
            cozuk = base64.b64decode(ham, validate=False)
        except Exception:
            cozuk = ham
        for kodlama in ("utf-8", "cp1254", "latin-1"):
            try:
                return cozuk.decode(kodlama)
            except UnicodeDecodeError:
                continue
        return cozuk.decode("utf-8", errors="replace")

    def _komut(self, command, **ek):
        params = {"command": command}
        if self.tpwd and command != "wlogin":
            params["tpwd"] = self.tpwd
        for k, v in ek.items():
            if v is None:
                continue
            params[k] = str(v)
        return self._istek(params)

    # --- oturum -------------------------------------------------------------
    def giris(self):
        md5 = hashlib.md5(self.cfg["parola"].encode("utf-8")).hexdigest().upper()
        yanit = self._komut(
            "wlogin",
            username=self.cfg["kullanici"],
            password=md5,
            devCode=self.cfg["dev_code"],
            devPass=self.cfg["dev_pass"],
            timeOut=self.cfg.get("timeout_dk", 60),
        )
        durum, _, mesaj = yanit.partition("&")
        if durum.strip() != "1":
            raise RuntimeError("SDK girişi başarısız: %s" % (mesaj.strip() or yanit[:200]))
        self.tpwd = mesaj.strip()
        LOG.info("SDK oturumu açıldı.")

    def cikis(self):
        if not self.tpwd:
            return
        try:
            self._komut("wlogout")
        except Exception as e:  # çıkış hatası kritik değil
            LOG.debug("wlogout hatası: %s", e)
        self.tpwd = None

    # --- veri ---------------------------------------------------------------
    def sirket_listesi(self):
        return self._komut("get_sirketliste")

    def stok_listesi(self):
        c = self.cfg
        return self._komut(
            "get_stoklist",
            sirketKodu=c["sirket_kodu"],
            calismaYili=c["calisma_yili"],
            ekSart=c.get("stok_ek_sart", ""),
            fieldList=c.get("stok_field_list", ""),
        )

    def stok_envanteri(self):
        c = self.cfg
        bugun = dt.date.today()
        sube_sart = ""
        if c.get("sube_kodu"):
            sube_sart = " AND SUBE_KODU='%s'" % c["sube_kodu"]
        return self._komut(
            "get_stokenvanter",
            sirketKodu=c["sirket_kodu"],
            calismaYili=c["calisma_yili"],
            envHesabi=c.get("envanter_hesabi", 1),
            maliyetTipi=c.get("envanter_maliyet_tipi", 5),
            tarih1="01.01.%s" % c["calisma_yili"],
            tarih2=bugun.strftime("%d.%m.%Y"),
            doviziDahilEt=0,
            sadeceMikEnv=1,
            stokEkSart=c.get("stok_ek_sart", ""),
            envSubeSart=sube_sart,
            fieldList="",
        )


# ----------------------------------------------------------------------------
# XML ayrıştırma (SDK'nın döndürdüğü yapıya toleranslı)
# ----------------------------------------------------------------------------

def xml_cozumle(metin):
    metin = metin.strip()
    if metin.startswith("Error") or metin.startswith("0&"):
        raise RuntimeError("SDK hata döndürdü: %s" % metin[:300])
    try:
        return ET.fromstring(metin)
    except ET.ParseError:
        # Bazı yanıtlarda baştaki BOM/boşluk veya '|*' kaçışı sorun çıkarabilir
        temiz = metin.replace("|*", "&amp;").lstrip("﻿")
        return ET.fromstring(temiz)


def satirlari_bul(kok, anahtar_alanlar):
    """Doğrudan çocukları arasında anahtar alanlardan birini taşıyan elemanlar = satır."""
    satirlar = []
    for el in kok.iter():
        cocuk_adlari = {c.tag.upper() for c in el}
        if cocuk_adlari & set(anahtar_alanlar):
            satirlar.append(el)
    return satirlar


def satir_sozluk(el):
    d = {}
    alt_listeler = {}
    for c in el:
        ad = c.tag.upper()
        if len(c):  # iç içe blok (ör. STOKFIYAT/FIYATLAR)
            alt_listeler.setdefault(ad, []).append(c)
        else:
            d[ad] = (c.text or "").strip()
    return d, alt_listeler


def fiyat_sec(d, alt_listeler, fiyat_no, adaylar):
    """Önce STOKFIYAT/FIYATLAR bloğundan satış fiyatı, yoksa düz alanlardan."""
    fiyat = None
    para = None
    for blok_adi, bloklar in alt_listeler.items():
        for blok in bloklar:
            for f in blok.iter():
                if f.tag.upper() != "FIYATLAR":
                    continue
                fd = {c.tag.upper(): (c.text or "").strip() for c in f}
                if fd.get("ALIS_SATIS", "2") != "2":
                    continue
                if fd.get("FIYAT_NO") and str(fd["FIYAT_NO"]) != str(fiyat_no):
                    continue
                fiyat = ondalik(fd.get("FIYATI"))
                para = fd.get("HESAP") or None
                if fiyat is not None:
                    return fiyat, para
    for a in adaylar:
        a_no = a.replace("1", str(fiyat_no)) if "1" in a else a
        for aday in (a_no, a):
            if aday in d:
                fiyat = ondalik(d[aday])
                if fiyat is not None:
                    return fiyat, d.get("DOVIZ_BIRIMI") or None
    return None, None


def urunleri_cikar(xml_metin, cfg):
    kok = xml_cozumle(xml_metin)
    satirlar = satirlari_bul(kok, ("STOKKODU", "BARKODU"))
    urunler = {}
    atlanan = 0
    for el in satirlar:
        d, altlar = satir_sozluk(el)
        barkod = barkod_temizle(d.get("BARKODU"))
        stok_kodu = (d.get("STOKKODU") or "").strip()
        if not barkod:
            atlanan += 1
            continue
        if d.get("AKTIF") not in (None, "", "1", "True", "true", "T"):
            continue
        fiyat, para = fiyat_sec(d, altlar, cfg.get("fiyat_no", 1), cfg.get("fiyat_alan_adaylari", []))
        kdv = ondalik(d.get("KDV_ORANI")) or 0.0
        if fiyat is not None and not cfg.get("fiyat_kdv_dahil", True):
            fiyat = round(fiyat * (1 + kdv / 100.0), 2)
        urunler[barkod] = {
            "barkod": barkod,
            "stok_kodu": stok_kodu,
            "ad": d.get("STOK_ADI") or d.get("ADI") or stok_kodu,
            "marka": d.get("MARKASI") or d.get("MARKA") or "",
            "grup": d.get("GRUBU") or d.get("GRUP") or "",
            "birim": d.get("BIRIMI") or d.get("BIRIM") or "",
            "kdv_orani": kdv,
            "fiyat": fiyat,
            "para_birimi": (para or d.get("DOVIZ_BIRIMI") or "TRY").replace("TL", "TRY").replace("₺", "TRY"),
            "stok_miktari": None,
            "aktif": 1,
        }
    LOG.info("Stok listesi: %d ürün barkodlu, %d barkodsuz atlandı.", len(urunler), atlanan)
    return urunler


def miktarlari_isle(xml_metin, urunler, cfg):
    kok = xml_cozumle(xml_metin)
    satirlar = satirlari_bul(kok, ("STOKKODU", "BARKODU", "BLSTKODU"))
    stok_koduna_gore = {u["stok_kodu"]: u for u in urunler.values() if u["stok_kodu"]}
    eslesen = 0
    for el in satirlar:
        d, _ = satir_sozluk(el)
        miktar = ondalik(ilk_dolu(d, cfg.get("miktar_alan_adaylari", [])))
        if miktar is None:
            continue
        hedef = None
        b = barkod_temizle(d.get("BARKODU"))
        if b and b in urunler:
            hedef = urunler[b]
        elif d.get("STOKKODU") in stok_koduna_gore:
            hedef = stok_koduna_gore[d["STOKKODU"]]
        if hedef is not None:
            hedef["stok_miktari"] = (hedef["stok_miktari"] or 0) + miktar
            eslesen += 1
    LOG.info("Envanter: %d satır ürünlerle eşleşti.", eslesen)


# ----------------------------------------------------------------------------
# API'ye gönderim
# ----------------------------------------------------------------------------

def api_post(api_cfg, yol, govde):
    url = api_cfg["url"].rstrip("/") + yol
    veri = json.dumps(govde, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url, data=veri, method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer %s" % api_cfg["token"],
            "User-Agent": "YapadaFiyatGorSync/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as y:
            return json.loads(y.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        govde_metin = e.read().decode("utf-8", errors="replace")
        raise RuntimeError("API %s -> HTTP %s: %s" % (yol, e.code, govde_metin[:300]))


def gonder(api_cfg, urunler):
    sync_id = dt.datetime.now().strftime("%Y%m%d%H%M%S") + "-" + uuid.uuid4().hex[:6]
    liste = list(urunler.values())
    sablon = api_cfg.get("resim_url_sablonu") or ""
    if sablon:
        for u in liste:
            u["resim_url"] = sablon.replace("{barkod}", u["barkod"]).replace("{stok_kodu}", urllib.parse.quote(u["stok_kodu"]))
    boyut = int(api_cfg.get("paket_boyutu", 500))
    toplam = 0
    for i in range(0, len(liste), boyut):
        paket = liste[i:i + boyut]
        sonuc = api_post(api_cfg, "/api/sync", {"sync_id": sync_id, "urunler": paket})
        toplam += int(sonuc.get("yazilan", len(paket)))
        LOG.info("Gönderildi: %d / %d", min(i + boyut, len(liste)), len(liste))
    bitis = api_post(api_cfg, "/api/sync/bitir", {"sync_id": sync_id, "adet": toplam, "kaynak": "wolvox-sdk"})
    LOG.info("Senkron tamamlandı. sync_id=%s, aktif ürün=%s, pasife alınan=%s",
             sync_id, bitis.get("aktif"), bitis.get("pasife_alinan"))
    return sync_id


# ----------------------------------------------------------------------------
# Ana akış
# ----------------------------------------------------------------------------

def tek_senkron(cfg, dry_run=False):
    w = cfg["wolvox"]
    sdk = WolvoxSDK(w)
    sdk.giris()
    try:
        xml_stok = sdk.stok_listesi()
        urunler = urunleri_cikar(xml_stok, w)
        if w.get("envanter_cek", True):
            try:
                xml_env = sdk.stok_envanteri()
                miktarlari_isle(xml_env, urunler, w)
            except Exception as e:
                LOG.warning("Envanter alınamadı, miktarsız devam ediliyor: %s", e)
    finally:
        sdk.cikis()

    if not urunler:
        raise RuntimeError("Hiç ürün çıkarılamadı. --kesfet ile alan adlarını kontrol edin.")

    if dry_run:
        with open("urunler.json", "w", encoding="utf-8") as f:
            json.dump(list(urunler.values()), f, ensure_ascii=False, indent=1)
        LOG.info("Dry-run: %d ürün urunler.json dosyasına yazıldı.", len(urunler))
        return None
    return gonder(cfg["api"], urunler)


def kesfet(cfg):
    w = cfg["wolvox"]
    sdk = WolvoxSDK(w)
    sdk.giris()
    try:
        xml_stok = sdk.stok_listesi()
        kok = xml_cozumle(xml_stok)
        satirlar = satirlari_bul(kok, ("STOKKODU", "BARKODU"))
        print("Kök etiket:", kok.tag, "| satır sayısı:", len(satirlar))
        if satirlar:
            d, altlar = satir_sozluk(satirlar[0])
            print("İlk satırın düz alanları:")
            for k, v in d.items():
                print("  %-28s %s" % (k, v[:60]))
            for ad, bloklar in altlar.items():
                print("İç içe blok:", ad, "(%d adet)" % len(bloklar))
                for c in list(bloklar[0].iter())[:25]:
                    if not len(c):
                        print("    %-26s %s" % (c.tag, (c.text or "").strip()[:40]))
        if w.get("envanter_cek", True):
            xml_env = sdk.stok_envanteri()
            kok2 = xml_cozumle(xml_env)
            satir2 = satirlari_bul(kok2, ("STOKKODU", "BARKODU", "BLSTKODU"))
            print("\nEnvanter kök etiket:", kok2.tag, "| satır sayısı:", len(satir2))
            if satir2:
                d2, _ = satir_sozluk(satir2[0])
                for k, v in d2.items():
                    print("  %-28s %s" % (k, v[:60]))
    finally:
        sdk.cikis()


def main(argv=None):
    p = argparse.ArgumentParser(description="Yapada Fiyat Gör — Wolvox SDK senkron")
    p.add_argument("--config", default="config.json")
    p.add_argument("--dongu", type=int, default=0, help="saniye; 0 = tek sefer")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--sirketler", action="store_true", help="get_sirketliste çıktısını yazdır")
    p.add_argument("--kesfet", action="store_true", help="SDK'nın döndürdüğü alan adlarını göster")
    p.add_argument("-v", "--verbose", action="store_true")
    a = p.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if a.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    with open(a.config, encoding="utf-8") as f:
        cfg = derin_birlestir(VARSAYILAN_CONFIG, json.load(f))

    if a.sirketler:
        sdk = WolvoxSDK(cfg["wolvox"])
        sdk.giris()
        try:
            print(sdk.sirket_listesi())
        finally:
            sdk.cikis()
        return 0
    if a.kesfet:
        kesfet(cfg)
        return 0

    while True:
        try:
            tek_senkron(cfg, dry_run=a.dry_run)
        except Exception as e:
            LOG.error("Senkron hatası: %s", e)
            if a.dongu <= 0:
                return 1
        if a.dongu <= 0:
            return 0
        time.sleep(a.dongu)


if __name__ == "__main__":
    sys.exit(main())
