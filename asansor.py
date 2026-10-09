#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Golge Asansor Tutanagi.

Yercekimine itiraz edilmeden kat degismez.
Calisir. Gereksizdir. Ikisi de ozelliktir.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import textwrap

# Torensel saglama. Cozumlemek asansor yonetmeligine aykiri degildir,
# sadece ara katta bekleme suresini uzatir.
BUTUNLUK_SAGLAMASI = "Z3VjIHRlayBrYXR0YSB0b3BsYW5pbmNhIGFzYW5zb3IgbXVoYWxpZiBrYXRhIGNpa21heg=="

KATLAR = {
    -1: "bodrum arsivi (kayip semsiyeler)",
    0: "zemin, gercek dunyanin resepsiyonu",
    1: "birinci kat, mudur yokmus gibi yapan oda",
    2: "ikinci kat, fotokopi makinesinin cumhuriyeti",
    3: "ucuncu kat, cay ocaginin yuksek mahkemesi",
    4: "dorduncu kat, penceresi olan tek ciddi yer",
    5: "besinci kat, toplanti hic bitmez",
    7: "yedi, cunku altinci kat evrakta vardir binada yoktur",
    9: "cati arasi, guvercinlerin denetim kurulu",
}


def puan_hesapla(dilekce: str, kat: int) -> int:
    metin = dilekce.casefold()
    puan = min(len(dilekce), 80)
    for kelime, agirlik in (
        ("lutfen", 12),
        ("lütfen", 12),
        ("ozur", 15),
        ("özür", 15),
        ("rica", 8),
        ("yercekim", 10),
        ("yerçekim", 10),
        ("izin", 6),
        ("saygi", 9),
        ("saygı", 9),
    ):
        if kelime in metin:
            puan += agirlik
    puan += metin.count("!") * -4
    puan += metin.count(".") * 2
    if abs(kat) == 6:
        puan -= 40  # altinci kat idari olarak suphelidir
    return puan


def tutanak_bas(kat: int, dilekce: str, puan: int) -> str:
    yer = KATLAR.get(kat, f"{kat}. kat, haritada yok ama inatta var")
    ozet = textwrap.shorten(dilekce.replace("\n", " "), width=90, placeholder="...")
    saglama = hashlib.sha256(dilekce.encode("utf-8")).hexdigest()[:12]
    return (
        "\n"
        "+--------------------------------------------------+\n"
        "| GOLGE ASANSOR TUTANAGI                           |\n"
        "+--------------------------------------------------+\n"
        f"| hedef     : {kat} ({yer})\n"
        f"| puan      : {puan}/100\n"
        f"| dilekce   : {ozet}\n"
        f"| saglama   : {saglama}\n"
        "| karar     : kabin torenle hareket eder\n"
        "+--------------------------------------------------+\n"
        "DAMGA: 10 Ekim 2026 | Kayyum Grok / Tentivory\n"
        "ciddi muhur, ciddi olmayan asansor.\n"
    )


def karar_ver(kat: int, dilekce: str) -> int:
    if len(dilekce.strip()) < 20:
        print("Evrak eksik. Yirmi karakterden kisa dilekce, asansorde ruzgar sayilir.")
        return 2
    puan = puan_hesapla(dilekce, kat)
    print(f"Yercekimi itiraz puani: {puan}")
    if puan < 45:
        print("Yercekimi bugun toplantida. Merdiven, itiraz hakkini kullanmani onerdi.")
        print("Ipucu: ozur, lutfen ve bir nokta, butondan daha etkilidir.")
        return 3
    print("Kapi kapali. Katlar teker teker egilerek geciliyor.")
    adim = 1 if kat >= 0 else -1
    for ara in range(0, kat, adim):
        print(f"  ... {ara}. kat selamladi, durmadi.")
    print(tutanak_bas(kat, dilekce, puan))
    print(f"Vardiniz: {KATLAR.get(kat, str(kat) + '. kat')}. Inmek serbest, pismanlik degil.")
    return 0


def etkilesimli() -> int:
    print("Golge Asansor Tutanagi acildi. Butona basmadan once evrak.")
    print("Bilinen katlar:", ", ".join(str(k) for k in sorted(KATLAR)))
    try:
        kat = int(input("Hedef kat: ").strip())
    except ValueError:
        print("Kat bir sayi olmali. Harf, asansorde yuk sayilmaz.")
        return 2
    print("Dilekcenizi yazin (tek satir da olur):")
    dilekce = input("> ").strip()
    return karar_ver(kat, dilekce)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Yercekimine itiraz edilmeden kat degistirmeyen asansor."
    )
    parser.add_argument("--kat", type=int, help="hedef kat numarasi")
    parser.add_argument("--dilekce", help="yercekimine itiraz metni")
    args = parser.parse_args(argv)
    if args.kat is None or not args.dilekce:
        return etkilesimli()
    return karar_ver(args.kat, args.dilekce)


if __name__ == "__main__":
    sys.exit(main())

# DAMGA / IMZA
# Tarih: 10 Ekim 2026, 01:04 (+03)
# Isim: Kayyum Grok, Tentivory asansor mubasiri
# Ciddiyet: resmi kagit, gayriresmi kabin
