import random
import math
from datetime import datetime

class Urun:
    def __init__(self, isim, fiyat, stok):
        self.isim = isim
        self.fiyat = fiyat
        self._stok = stok
        self.barkod = random.randint(100000, 999999)

    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, miktar):
        if miktar < 0:
            print("Stok negatif olamaz!")
        else:
            self._stok = miktar

class Musteri:
    def __init__(self, ad, email):
        self.ad = ad
        self.email = email
        self.sepet = []
        self.siparis_gecmisi = []

    def sepete_ekle(self, urun):
        if urun.stok > 0:
            self.sepet.append(urun)
            print(f"{urun.isim} sepete eklendi.")
        else:
            print(f"Üzgünüz, {urun.isim} stokta yok.")

    def __contains__(self, urun_isim):
        # Müşterinin sepetinde ürün ismine göre kontrol
        return any(u.isim == urun_isim for u in self.sepet)

class Siparis:
    def __init__(self, musteri):
        self.musteri = musteri
        self.siparis_no = random.randint(1000, 9999)
        self.siparis_tarihi = datetime.now()
        self.toplam_tutar = 0

    def odeme_yap(self):
        if not self.musteri.sepet:
            print("Sepet boş.")
            return

        ham_tutar = sum(u.fiyat for u in self.musteri.sepet)
        kdvli_tutar = ham_tutar * 1.18
        # Math modülü ile yukarı yuvarlama (kuruş farkı için)
        self.toplam_tutar = math.ceil(kdvli_tutar) 
        
        print(f"Sipariş No: {self.siparis_no}")
        print(f"Tarih: {self.siparis_tarihi}")
        print(f"Ödenecek Tutar (%18 KDV Dahil): {self.toplam_tutar} TL")
        self.stok_guncelle()
        
        # Geçmişe ekle ve sepeti boşalt
        self.musteri.siparis_gecmisi.append(self)
        self.musteri.sepet = []

    def stok_guncelle(self):
        for urun in self.musteri.sepet:
            urun.stok -= 1

# Örnek Kullanım
u1 = Urun("Laptop", 15000, 5)
u2 = Urun("Mouse", 500, 20)

m1 = Musteri("Zeynep", "zeynep@mail.com")
m1.sepete_ekle(u1)
m1.sepete_ekle(u2)

if "Laptop" in m1:
    print("Müşteri sepetinde Laptop var.")

siparis = Siparis(m1)
siparis.odeme_yap()
print(f"Laptop Yeni Stok: {u1.stok}")
