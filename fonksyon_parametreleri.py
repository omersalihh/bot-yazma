ad = input("adınız: ")
soy = input("soyadınız: ")
notlar = input("sınav notları (virgülle ayrılmış)")
print(notlar)
notlar_list = [int(x)for x in notlar.split(",")]
ortalama = sum(notlar_list)/len(notlar_list)

dosya = open("öğrenciler.txt", mod="a")
dosya.write(f"ad:{ad} , soyad:{soy} , notlar:{notlar} , ortalama:{notlar_list}")
