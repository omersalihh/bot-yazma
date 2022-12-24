#boş bir liste tanımlayalım
liste = [1,2,3,4,5,6,7,8,9]

okul = "teknoloji imam hatip lisesi"
kelimeler = okul.split()
print(kelimeler[2])

ad = "ömer salih öztürk"
print(ad[0])
print(ad[5:10])
print(ad[5:10:3])
print(ad[ : : -1])


a = [[1, 2, 3] ,[4, 5, 6], [7, 8, 9]]
for x in a:
    for y in x:
        print(y, end=' ')
    print()


#listeler içerisinde farklı türde veriler olabilir
list = [1, 5.4, "sa", True, [1,2,3]]
print(list[-1] [-1])
print(list[4][2])

liste2 =[1,2,3]
liste3 =[4,5,6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2