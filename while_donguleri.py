# i = 1
# while i < 101:
#     if (i % 2 == 0):
#         print(f"{i} Sayı Çift")
#     else:
#         print(f"{i} Sayı Tek")
#     i += 1

import xlrd

ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

cs = ck.sheet_by_index(0)
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print((f"satır sayısı: {satir_sayisi}"))
print((f"sutun sayısı: {sutun_sayisi}"))
i = 0
a1 = cs.cell(i,6)
print(a1)


while i <37785:
    olay = cs.cell_value(i,8)
    futbolcu = cs.cell_value(i, 6)
    i += 1
    print(f"oyuncu: {futbolcu} - olay: {olay}")


