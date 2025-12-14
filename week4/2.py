import math
from collections import Counter

class Ogrenci:
    def __init__(self, ad, soyad, ogrenci_no):
        self.ad = ad
        self.soyad = soyad
        self.ogrenci_no = ogrenci_no
        self.ders_notlari = {}
        self.not_istatistigi = Counter()

    def not_ekle(self, ders_adi, notlar):
        self.ders_notlari[ders_adi] = notlar
        # İstatistik için notları grupluyoruz (Örn: 90'lar, 80'ler gibi basit istatistik)
        for not_degeri in notlar:
            aralik = (not_degeri // 10) * 10
            self.not_istatistigi[f"{aralik}-{aralik+9}"] += 1
        print(f"{ders_adi} notları eklendi. İstatistik: {self.not_istatistigi}")

    def ortalama_hesaplama(self):
        # Base class varsayılan hesaplama (düz ortalama ve ceil)
        if not self.ders_notlari:
            return 0
        tum_notlar = [n for notlar in self.ders_notlari.values() for n in notlar]
        ortalama = sum(tum_notlar) / len(tum_notlar)
        return math.ceil(ortalama)

class LisansOgrencisi(Ogrenci):
    def ortalama_hesaplama(self):
        # Override: Floor kullanımı
        if not self.ders_notlari:
            return 0
        tum_notlar = [n for notlar in self.ders_notlari.values() for n in notlar]
        ortalama = sum(tum_notlar) / len(tum_notlar)
        return math.floor(ortalama)

class YuksekLisansOgrencisi(Ogrenci):
    def ortalama_hesaplama(self):
        # Override: Farklı kriter (Örn: En düşük notu atıp hesapla)
        if not self.ders_notlari:
            return 0
        tum_notlar = sorted([n for notlar in self.ders_notlari.values() for n in notlar])
        if len(tum_notlar) > 1:
            tum_notlar = tum_notlar[1:] # En düşüğü at
        ortalama = sum(tum_notlar) / len(tum_notlar)
        return round(ortalama, 2)

# Örnek Kullanım
ogrenci1 = LisansOgrencisi("Ayşe", "Yılmaz", "2021001")
ogrenci1.not_ekle("Matematik", [85, 90, 78])
print(f"Lisans Ortalaması (Floor): {ogrenci1.ortalama_hesaplama()}")

ogrenci2 = YuksekLisansOgrencisi("Ali", "Kaya", "2022999")
ogrenci2.not_ekle("İleri Fizik", [60, 90, 85])
print(f"Yüksek Lisans Ortalaması (Özel): {ogrenci2.ortalama_hesaplama()}")
