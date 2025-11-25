print("---Hoş geldiniz öğrenci takip sistemine--- ")
ogrenci_listesi = []
ogrenci_sayisi = int(input("Kaç öğrenci eklemek istiyorsunuz?: \n"))

for i in range(ogrenci_sayisi):
    isim = input("Öğrenci adı: \n")
    soyisim = input("Öğrenci soyadı: \n")
    vize_notu = int(input("Vize notu: \n"))
    final_notu = int(input("Final notu: \n"))
    ogrenci_ortalamasi = (vize_notu * 0.4) + (final_notu * 0.6)
    ogrenci = {"Ad": f"{isim}",
               "Soyad": f"{soyisim}",
               "Vize Notu": vize_notu,
               "Final Notu": final_notu,
               "Ortalama": ogrenci_ortalamasi,
               "Durum": ""}
    if ogrenci_ortalamasi >= 50:
        ogrenci["Durum"] = "Geçti"
    else:
        ogrenci["Durum"] = "Kaldı"

    ogrenci_listesi.append(ogrenci)

print(f"{'Ad':<10} {'Soyad':<10} {'Vize':<7} {'Final':<6} {'Ort':<5} {'Durum'}")
print("-" * 55)

for ogrenci in ogrenci_listesi:
    print(f"{ogrenci['Ad']:<10} {ogrenci['Soyad']:<10} "
          f"{ogrenci['Vize Notu']:<7} {ogrenci['Final Notu']:<6} "
          f"{ogrenci['Ortalama']:<5.2f} {ogrenci['Durum']}")