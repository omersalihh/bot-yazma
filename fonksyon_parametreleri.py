ad = input("adınız: ")
soy = input("soyadınız: ")
notlar = input("sınav notları (virgülle ayrılmış)")

notlar_list = [int(x)for x in notlar.split(",")]
ortalama = sum(notlar_list)/len(notlar_list)

dosya = open("ogreniler.txt",   mode="a")
dosya.write(f"ad:{ad} , soyad:{soy} , notlar:{notlar} , ortalama:{notlar_list}")
