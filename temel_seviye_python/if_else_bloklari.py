"""
if ve else blokları ile mantıksal operayörler kullamak
programın akışını etkileyebilir
"""
#kullanıcıdan 2 sayı alalım
#hangi sayı büyükse ekrana yazdır

sayi1 = int(input("1. sayıyı giriniz"))
sayi2 = int(input("2. sayıyı giriniz"))


if sayi1 > sayi2:
     print(f"1.sayi({sayi1}) 2.sayıdan ({sayi2}) büyüktür")
else:
    print(f"2.sayi({sayi2}) 1.sayıdan ({sayi1}) büyüktür")