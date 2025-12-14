from datetime import datetime

class BankaHesabi:
    def __init__(self, hesap_no, bakiye, hesap_turu):
        self.hesap_no = hesap_no
        self.bakiye = bakiye
        self.hesap_turu = hesap_turu
        self.hesap_acilis_tarihi = datetime.now()
        self.islem_gecmisi = []
        self._gecmis_ekle(f"Hesap açıldı. İlk Bakiye: {bakiye} TL")

    def _gecmis_ekle(self, islem):
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.islem_gecmisi.append(f"{zaman} - {islem}")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            self._gecmis_ekle(f"Para Yatırma: +{miktar} TL")
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar.")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Uyarı: Yetersiz bakiye!")
        elif miktar > 0:
            self.bakiye -= miktar
            self._gecmis_ekle(f"Para Çekme: -{miktar} TL")
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar.")

    def hesap_raporu(self):
        print(f"\n--- {self.hesap_no} Nolu Hesap Dökümü ---")
        for islem in self.islem_gecmisi:
            print(islem)
        print(f"Güncel Bakiye: {self.bakiye} TL")

    def __str__(self):
        return f"{self.hesap_no} nolu hesap – Bakiye: {self.bakiye} TL – Tür: {self.hesap_turu}"

    def __add__(self, other):
        if isinstance(other, BankaHesabi):
            return self.bakiye + other.bakiye
        return NotImplemented

# Örnek Kullanım
hesap1 = BankaHesabi("12345", 1000, "Vadesiz")
hesap2 = BankaHesabi("67890", 5000, "Vadeli")

hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.para_cek(2000) # Yetersiz bakiye uyarısı

print("\n" + str(hesap1))
print(f"İki hesabın toplamı: {hesap1 + hesap2} TL")
hesap1.hesap_raporu()
