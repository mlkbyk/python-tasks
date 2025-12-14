from datetime import datetime, timedelta

class Personel:
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi_str):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman
        # Tarih formatı: YYYY-MM-DD
        self.ise_baslama_tarihi = datetime.strptime(ise_baslama_tarihi_str, "%Y-%m-%d")

    def zam_hesapla(self):
        bugun = datetime.now()
        calisma_suresi = bugun - self.ise_baslama_tarihi
        yil = calisma_suresi.days / 365
        
        # Basit kıdem mantığı
        if yil < 1: return "%0"
        elif yil < 3: return "%10"
        else: return "%20"

    def izin_hesapla(self):
        bugun = datetime.now()
        calisma_suresi = bugun - self.ise_baslama_tarihi
        # Her yıl için 14 gün izin
        hakedilen_izin = (calisma_suresi.days // 365) * 14
        return f"{hakedilen_izin} gün"

    def __eq__(self, other):
        if isinstance(other, Personel):
            return self.maas == other.maas
        return False

    def __gt__(self, other):
        # Kıdem kontrolü: Tarihi daha küçük olan (daha eski başlayan) daha kıdemlidir.
        if isinstance(other, Personel):
            return self.ise_baslama_tarihi < other.ise_baslama_tarihi
        return False

class Yonetici(Personel):
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi_str, sorumlu_kisiler=None):
        super().__init__(ad, soyad, maas, departman, ise_baslama_tarihi_str)
        self.sorumlu_oldugu_kisiler = sorumlu_kisiler if sorumlu_kisiler else []

    def bonus_hesapla(self):
        return self.maas * 0.20 # Yönetici bonusu

class Gelistirici(Personel):
    def __init__(self, ad, soyad, maas, departman, ise_baslama_tarihi_str, tech_stack=None):
        super().__init__(ad, soyad, maas, departman, ise_baslama_tarihi_str)
        self.tech_stack = tech_stack if tech_stack else []

    def proje_primi_hesapla(self, proje_sayisi):
        return proje_sayisi * 1000

# Örnek Kullanım
personel1 = Yonetici("Mehmet", "Demir", 20000, "IT", "2020-03-15")
personel2 = Gelistirici("Zeynep", "Kaya", 15000, "Yazılım", "2021-06-20")

print(f"Kıdem (Mehmet > Zeynep): {personel1 > personel2}") # True dönerse Mehmet daha eski çalışan
print(f"Maaş Eşitliği: {personel1 == personel2}")
print(f"Mehmet Zam Oranı: {personel1.zam_hesapla()}")
print(f"Zeynep İzin Hakkı: {personel2.izin_hesapla()}")
