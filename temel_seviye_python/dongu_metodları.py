'''list = list(range(1,10))
print(list)
'''
for i in range(50):
    print(f"{i+1}. python")



kelime = "python"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)

for harf in kelime:
    print(harf)

sayilar = [1,2,3]
okunuslar = ["bir","iki","üç"]
sayilar_zip = list(zip(sayilar,okunuslar))
print(sayilar_zip)
for sayi, okunus in zip(sayilar,okunuslar):
    print(sayi,okunus)
