#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wolvox SDK taklidi (yalnızca test için).

Gerçek SDK gibi davranır: istek parametreleri Base64 kodlu gelir, yanıt Base64
kodlu döner; wlogin, wlogout, get_sirketliste, get_stoklist, get_stokenvanter
komutlarını örnek Yapada ürünleriyle cevaplar.

  python mock_sdk_server.py --port 3056
"""
import argparse
import base64
import hashlib
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from xml.sax.saxutils import escape

DEV_CODE = "DEMO"
DEV_PASS = "DEMO"
KULLANICI = "SYSDBA"
PAROLA = "masterkey"
TPWD = "55884AE673175EC1C1171FEBBE2C235A"

URUNLER = [
    # barkod, stok kodu, ad, marka, grup, kdv, fiyat (KDV dahil), miktar
    ("887961953404", "HW-GHF46", "Hot Wheels Tekli Araba Nissan Skyline GT-R (R34)", "Hot Wheels", "Koleksiyon", 20, 149.90, 12),
    ("4895183661317", "MGT00412", "Mini GT 1:64 Porsche 911 GT3 RS Shark Blue", "Mini GT", "Koleksiyon", 20, 899.00, 2),
    ("889698712019", "FUNKO-15033", "Funko Pop! Marvel Spider-Man No Way Home #1160", "Funko", "Koleksiyon", 20, 749.00, 0),
    ("8018190034578", "PAN-WC26-BOX", "Panini FIFA World Cup 2026 Sticker Kutusu (50 paket)", "Panini", "Kırtasiye", 20, 1875.00, 7),
    ("4005401104230", "FC-110423", "Faber-Castell Grip 2001 Kurşun Kalem B", "Faber-Castell", "Kırtasiye", 20, 29.50, 140),
    ("5010993843985", "HAS-F4651", "Monopoly Türkiye Baskısı", "Hasbro", "Oyuncak", 20, 1299.00, 4),
    ("673419373616", "LEGO-76917", "LEGO Speed Champions Nissan Skyline GT-R (R34) 2 Fast 2 Furious", "LEGO", "Oyuncak", 20, 1049.00, 1),
    ("8690345678901", "YPD-HED-001", "Yapada Hediye Kartı 500 TL", "Yapada", "Hediye", 0, 500.00, 999),
]


def xml_stoklist():
    satirlar = []
    for b, kod, ad, marka, grup, kdv, fiyat, _ in URUNLER:
        satirlar.append(
            "<STOK>"
            "<BLKODU>%d</BLKODU><STOKKODU>%s</STOKKODU><STOK_ADI>%s</STOK_ADI>"
            "<BARKODU>%s</BARKODU><GRUBU>%s</GRUBU><MARKASI>%s</MARKASI>"
            "<BIRIMI>ADET</BIRIMI><KDV_ORANI>%d</KDV_ORANI><AKTIF>1</AKTIF>"
            "<STOKFIYAT><FIYATLAR><FIYAT_NO>1</FIYAT_NO><FIYATI>%s</FIYATI><HESAP>TL</HESAP>"
            "<ALIS_SATIS>2</ALIS_SATIS><TANIMI>SATIŞ FİYATI -1</TANIMI></FIYATLAR>"
            "<FIYATLAR><FIYAT_NO>1</FIYAT_NO><FIYATI>%s</FIYATI><HESAP>TL</HESAP>"
            "<ALIS_SATIS>1</ALIS_SATIS><TANIMI>ALIŞ FİYATI -1</TANIMI></FIYATLAR></STOKFIYAT>"
            "</STOK>"
            % (len(satirlar) + 1, escape(kod), escape(ad), b, escape(grup), escape(marka), kdv,
               ("%.2f" % fiyat).replace(".", ","), ("%.2f" % (fiyat * 0.6)).replace(".", ","))
        )
    return '<?xml version="1.0" encoding="UTF-8"?><STOKLAR>%s</STOKLAR>' % "".join(satirlar)


def xml_envanter():
    satirlar = []
    for i, (b, kod, ad, _, _, _, _, miktar) in enumerate(URUNLER, 1):
        satirlar.append(
            "<ENVANTER><BLSTKODU>%d</BLSTKODU><STOKKODU>%s</STOKKODU><STOK_ADI>%s</STOK_ADI>"
            "<BARKODU>%s</BARKODU><KALAN_MIKTAR>%s</KALAN_MIKTAR><BIRIMI>ADET</BIRIMI></ENVANTER>"
            % (i, escape(kod), escape(ad), b, ("%.2f" % miktar).replace(".", ","))
        )
    return '<?xml version="1.0" encoding="UTF-8"?><STOKENVANTER>%s</STOKENVANTER>' % "".join(satirlar)


def xml_sirketler():
    return ('<?xml version="1.0" encoding="UTF-8"?><SIRKETLER><SIRKET><SIRKET_KODU>YAPADA</SIRKET_KODU>'
            '<UNVANI>YAPADA DÜKKAN</UNVANI><CALISMA_YILI>2026</CALISMA_YILI><SUBE_KODU>MERKEZ</SUBE_KODU>'
            '</SIRKET></SIRKETLER>')


def isle(sorgu):
    params = dict(urllib.parse.parse_qsl(sorgu, keep_blank_values=True, strict_parsing=False)) \
        if "%" in sorgu else {k: v for k, _, v in (p.partition("=") for p in sorgu.split("&"))}
    cmd = params.get("command", "")
    if cmd == "wlogin":
        md5 = hashlib.md5(PAROLA.encode()).hexdigest().upper()
        ok = (params.get("username") == KULLANICI and params.get("password", "").upper() == md5
              and params.get("devCode") == DEV_CODE and params.get("devPass") == DEV_PASS)
        return "1&" + TPWD if ok else "0&Geçersiz kullanıcı adı yada parolası."
    if params.get("tpwd") != TPWD:
        return "0&Oturum bulunamadı."
    if cmd == "wlogout":
        return "1&"
    if cmd == "get_sirketliste":
        return xml_sirketler()
    if cmd == "get_stoklist":
        return xml_stoklist()
    if cmd == "get_stokenvanter":
        return xml_envanter()
    return "Error : Bilinmeyen komut %s" % cmd


class H(BaseHTTPRequestHandler):
    def _yanit(self, metin):
        govde = base64.b64encode(metin.encode("utf-8"))
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(govde)))
        self.end_headers()
        self.wfile.write(govde)

    def do_GET(self):
        yol, _, kodlu = self.path.partition("?")
        if not yol.endswith("getdata.html"):
            self.send_error(404)
            return
        sorgu = base64.b64decode(kodlu + "=" * (-len(kodlu) % 4)).decode("utf-8")
        self._yanit(isle(sorgu))

    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        govde = self.rfile.read(n).decode("utf-8")
        kodlu = govde.split("DATA=", 1)[-1]
        sorgu = base64.b64decode(kodlu + "=" * (-len(kodlu) % 4)).decode("utf-8")
        self._yanit(isle(sorgu))

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=3056)
    a = ap.parse_args()
    print("Sahte Wolvox SDK http://127.0.0.1:%d/getdata.html  (SYSDBA/masterkey, devCode DEMO/DEMO)" % a.port)
    HTTPServer(("127.0.0.1", a.port), H).serve_forever()
