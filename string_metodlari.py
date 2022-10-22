okul = "teknLoloji  imamhATip  liSesi"

#tüm karakterleri büyük harf yapalım
print(okul.upper())

#tüm karakterleri küçük yapma
print(okul.lower())

#her kelimenin ilk harfini büyük yapalım
print(okul.title())

#karakter dizisinin ilk karakterini büyük, diğer karakterlerini
#küçük harf yapalım: capitalize(
print(okul.capitalize())

#belirli bir ifadenin kaç defa yer aldığını bulalım
makale = "Adaptasyon, uyum başarısı ile yakından ilişkilidir. Uyum başarısını ilgi duyulan konuya bağlı olarak farklı şekillerde ölçmek mümkündür: ömür (hafta veya yıl olarak), doğan yavru sayısı, üretilen sperm sayısı, doğan sağlıklı yavru sayısı, üreme çağına erişebilen yavru sayısı ve daha nicesi... Ancak ne olursa olsun, pozitif (doğal) seçilim bakısı altında olan özellikler, uyum başarısının artacağı yönde seçilir. Bu seçilim baskısı, genellikle çevrenin değişimine bağlı olarak tetiklenir: Ortama giren yeni bir avcı, besin erişiminde yaşanan kısıtlar, iklimin değişmesi, bitki örtüsünde yaşanan değişmeler, asidite ve sıcaklık gibi değişimler ve daha nicesi... "
print(okul.count("e"))
print(okul.lower().count("a"))
print(makale.lower().count("yavru"))

#soldaki ya da sağdaki boşluk karakterlerini temizleyelim : strip()
ad = input("adınız : ")
print(ad.strip())

#soldaki ve sağdaki belirli karakterleri temizleyelim strip("ifdade")
urun_kod = "HEP20221022HEP"
print(urun_kod.strip("HEP"))

#soldaki boşluk veya belirli ifadeyi temizleyelim: lstrip
print("sa" + ad + "as")
print(ad.lstrip() + "sa")

#sağ boşluk veya belirli ifadeyi temizleyelim: lstrip
print("sa" + ad + "as")
print(ad.rstrip() + "as")

#karakter dizisini bölelim: split()
print(okul.split()) #parantezin içine neyi yazarsak o karakterlerden böler

#böldüğümüz ve listeye dönüşen ifadeleri birleştirelim: join()
kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

print("AHMET KAYA".center(25,"-"))