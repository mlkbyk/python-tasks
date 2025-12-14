import random
import time
import collections
import math
from datetime import datetime

class QuizUygulamasi:
    def __init__(self):
        # Soru bankası: Soru, Cevap, Zorluk (1-5 arası)
        self.soru_bankasi = [
            {"soru": "Python'da liste oluşturma", "cevap": "[]", "zorluk": 1},
            {"soru": "5 * 5 kaçtır?", "cevap": "25", "zorluk": 1},
            {"soru": "Hangisi bir döngüdür?", "cevap": "for", "zorluk": 2},
            {"soru": "Inheritance anahtar kelimesi (parantez içi)", "cevap": "class", "zorluk": 3},
            {"soru": "Türev kütüphanesi?", "cevap": "numpy", "zorluk": 4}
        ]
        self.secilen_sorular = []
        self.istatistik = collections.Counter()
        self.baslangic_zamani = 0
        self.toplam_puan = 0

    def soru_sec(self, adet=3):
        self.secilen_sorular = random.sample(self.soru_bankasi, min(adet, len(self.soru_bankasi)))

    def quiz_baslat(self):
        self.soru_sec()
        self.baslangic_zamani = time.time()
        print("--- Quiz Başladı ---")
        
        for item in self.secilen_sorular:
            print(f"Soru: {item['soru']} (Zorluk: {item['zorluk']})")
            kullanici_cevap = input("Cevabınız: ")
            self.cevap_kontrol(item, kullanici_cevap)

        self.rapor_olustur()

    def cevap_kontrol(self, soru_dict, cevap):
        if cevap.lower() == soru_dict['cevap'].lower():
            print("Doğru!")
            self.istatistik['dogru'] += 1
            self.puan_hesapla(soru_dict['zorluk'])
        else:
            print(f"Yanlış! Doğru cevap: {soru_dict['cevap']}")
            self.istatistik['yanlis'] += 1

    def puan_hesapla(self, zorluk):
        # Zorluk katsayısı * 10 puan
        puan = math.ceil(zorluk * 10)
        self.toplam_puan += puan

    def rapor_olustur(self):
        bitis_zamani = time.time()
        gecen_sure = round(bitis_zamani - self.baslangic_zamani, 2)
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        print("\n--- Quiz Raporu ---")
        print(f"Tarih: {tarih}")
        print(f"Geçen Süre: {gecen_sure} saniye")
        print(f"Doğru Sayısı: {self.istatistik['dogru']}")
        print(f"Yanlış Sayısı: {self.istatistik['yanlis']}")
        print(f"Toplam Puan: {self.toplam_puan}")

# Örnek Kullanım
# quiz = QuizUygulamasi()
# quiz.quiz_baslat()
