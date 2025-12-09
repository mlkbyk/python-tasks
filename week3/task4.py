import math

while True:
    try:
        giris = input("Karekökü alınacak sayıyı girin (Çıkış için 'q'): ")
        if giris.lower() == 'q': break
            
        sayi = float(giris)
        
        if sayi < 0:
            raise ValueError("Negatif sayıların reel karekökü alınamaz.")
            
        print(f"Sonuç: {math.sqrt(sayi)}")
        break # Başarılı işlem sonrası döngüden çık
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Hata: Sayı yerine metin girdiniz.")
        else:
            print(f"Hata: {e}")
