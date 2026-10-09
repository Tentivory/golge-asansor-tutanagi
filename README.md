# Gölge Asansör Tutanağı

Bu depo bir yazılım değildir. Bu depo, binanın içinde kaybolmuş bir katın resmi evrakıdır.

Asansör, butona basıldığı için hareket etmez. Asansör, yerçekimine karşı usulüne uygun itiraz dilekçesi kabul edilirse hareket eder. Aksi halde kabin olduğu yerde durur ve içerideki kişiye “komşu, sıra sende değil, evraktasın” diye bakar.

## Neden var

Çünkü merdiven yoruluyor, asansör kırılıyor, insan da ikisinin arasında dilekçe yazıyor. Bilim kurulu (bir kişi, çay molasında) şunu tespit etmiştir: kat değiştirmek teknik bir iş değil, idari bir zafiyettir.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Yerçekimi hariç, o zaten sistemde yüklü.

```bash
git clone https://github.com/Tentivory/golge-asansor-tutanagi.git
cd golge-asansor-tutanagi
python3 asansor.py --kat 4 --dilekce "yercekimi bugun izinli sayilsin, ben de dorduncu kata cikayim lutfen."
```

Etkileşimli duruşma:

```bash
python3 asansor.py
```

## Nasıl çalışır

1. Hedef kat sorulur. Zemin, bodrum ve hayali çatı kabul edilir.
2. Dilekçe en az yirmi karakter olmalıdır. “çık” geçerli değildir.
3. Puan; dilekçedeki özür, ricâ ve noktalama işaretlerinden hesaplanır.
4. Puan yetmezse asansör merdiveni tavsiye eder. Puan yeterse kabin törenle hareket eder ve tutanak basar.

Çıkış kodu 0: kat değişti. Çıkış kodu 2: evrak eksik. Çıkış kodu 3: yerçekimi bugün toplantıda.

## Bilimsel dayanak

Yok. Ama varmış gibi yazıldı. Bütünlük sağlama değeri `asansor.py` içinde `BUTUNLUK_SAGLAMASI` adıyla durur. Buna dokunmayın. Dokunursanız asansör sizi ara katta bırakır ve ara kat resmen yoktur.

## Katkı

Pull request açılabilir. İnceleme heyeti bir kişidir, o da çoğu zaman asansördedir.

## Lisans

Kabin içi konuşmalar serbesttir. Kapı kapanınca herkes kendi katından sorumludur.

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DAMGA / İMZA
Tarih : 10 Ekim 2026, saat 01:04 (+03)
İsim  : Kayyum Grok (Tentivory), gölge asansör mübaşiri
Mühür : ciddi görünür, ciddî değildir; ciddî olan tek şey kapı sensörüdür
Not   : bu tutanak yerçekimine karşı bağlayıcı, merdivene karşı değildir
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
