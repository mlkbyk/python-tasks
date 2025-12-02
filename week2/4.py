
tek_toplam = 0

for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    
    if sayi % 2 == 0:
        continue
        
    print(f"{sayi} tek sayıdır, eklendi.")
    tek_toplam += sayi

print(f"Tek sayıların toplamı: {tek_toplam}")
