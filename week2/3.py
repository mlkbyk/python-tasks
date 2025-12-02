
import random

hedef = random.randint(1, 100)
hak = 10

while hak > 0:
    tahmin = int(input(f"Kalan hak {hak}. Tahmininiz: "))
    
    if tahmin == hedef:
        print("Tebrikler, doğru tahmin!")
        break
    elif tahmin < hedef:
        print("Daha büyük bir sayı girin.")
    else:
        print("Daha küçük bir sayı girin.")
        
    hak -= 1

if hak == 0:
    print(f"Oyun bitti. Sayı: {hedef}")
