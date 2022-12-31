#tarayıcı nesnemizi import edelim
from moduller.tarayici import Tarayici
from time import sleep

tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

# Tarayıcıda gezinme
tarayici.get("https://minecraftevi.com/")
print(tarayici.current_url)
sleep(1)

# yeni adrese gidelim
tarayici.get("https://burakoyunda.com/")
print(tarayici.title)
sleep(1)

# geri dönelim
tarayici.back()
print(tarayici.title)
sleep(1)

# ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(1)

# pencere boyutunu yazdıralım
print(tarayici.get_window_size())

# pencere boyutu ayarlayalım
tarayici.set_window_size(500, 300)
sleep(2)

# pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.set_window_position(100, 500)
sleep(2)

#tam ekran yapalım
tarayici.maximize_window()
sleep(2)
tarayici.fullscreen_window()
sleep(2)


#simge yapalım
tarayici.minimize_window()
sleep(2)

#ekran görüntüsü alma

tarayici.save_screenshot("./foto/foto1.png")
