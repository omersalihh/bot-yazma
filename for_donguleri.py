elemanlar = ["ahmety","mehmeyt","sa"]

for eleman in elemanlar:
    print(f"eleman adı : {eleman}")
sayilar= [(1, 2), (3, 4), (5, 6)]
for x, y in sayilar:
    print(f"1.sayi: {x}   2. sayi: {y}")

okul = "sancaktepe tekonoloji adamdolu imamhatip lisesi"
for a in okul.split():
    print(f"{a}")

adamlar = {
    1: {
        "ad": "ahmet",
        "soyad": "bozkurt",
        "cinsiyet": True,
        "dersler": ["mat"]
    },
    45: {
        "ad": "muharrem",
        "soyad": "pro",
        "cinsiyet": False,
        "dersler": ["mat"]
    }
}
for no,adam in adamlar.items():
    print(f"{no} numaralı adam : {adam['ad']}")