import os
import random
import re
import string

class DosyaYoneticisi:
    def __init__(self, calisma_dizini="."):
        self.calisma_dizini = calisma_dizini

    def dosya_olustur(self, icerik="Varsayılan içerik"):
        # Rastgele dosya ismi (5 harfli)
        isim = ''.join(random.choices(string.ascii_lowercase, k=5)) + ".txt"
        yol = os.path.join(self.calisma_dizini, isim)
        
        with open(yol, "w", encoding="utf-8") as f:
            f.write(icerik)
        print(f"Dosya oluşturuldu: {isim}")
        return isim

    def dosya_oku_regex(self, dosya_adi, pattern):
        yol = os.path.join(self.calisma_dizini, dosya_adi)
        if os.path.exists(yol):
            with open(yol, "r", encoding="utf-8") as f:
                icerik = f.read()
                eslesmeler = re.findall(pattern, icerik)
                return eslesmeler
        return []

    def klasor_tarama(self):
        dosyalar = os.listdir(self.calisma_dizini)
        print(f"Klasördeki dosyalar: {dosyalar}")
        return dosyalar

    def __len__(self):
        return len([d for d in os.listdir(self.calisma_dizini) if os.path.isfile(os.path.join(self.calisma_dizini, d))])

# Örnek Kullanım
# Not: Bu kod çalıştırıldığı dizinde dosya oluşturur.
dy = DosyaYoneticisi()
dosya_isim = dy.dosya_olustur("Python 123 ve Java 456 dersleri.")
eslesme = dy.dosya_oku_regex(dosya_isim, r"\d+") # Sayıları bul
print(f"Bulunan desenler: {eslesme}")
dy.klasor_tarama()
print(f"Toplam dosya sayısı: {len(dy)}")
