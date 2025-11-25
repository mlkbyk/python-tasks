sicakliklar = [22.5, 23.1, 21.8, 19.5, 18.9, 20.2, 22.7, 24.3, 25.6, 26.2, 25.8,
24.9, 23.7, 22.4, 21.1, 20.8, 19.9, 18.7, 19.2, 20.5, 21.9, 23.3, 22.8, 21.5]

print("--- Konfor Analizi ---")
for saat, sicaklik in enumerate(sicakliklar):
    if not 20 <= sicaklik <= 24:
        print(f"Saat {saat}: {sicaklik}°C - Konfor aralığı dışında!")

print("\n--- Enerji Tüketimi Uyarısı ---")
klima_calisma_saati = 0
isitici_calisma_saati = 0
for sicaklik in sicakliklar:
    if sicaklik > 25:
        klima_calisma_saati += 1
    if sicaklik < 18:
        isitici_calisma_saati += 1
print(f"Klima çalışma saati: {klima_calisma_saati}")
print(f"Isıtıcı çalışma saati: {isitici_calisma_saati}")

print("\n--- Gün İçi Sıcaklık Farkı ---")
maksimum_sicaklik = max(sicakliklar)
minimum_sicaklik = min(sicakliklar)
sicaklik_farki = round(maksimum_sicaklik - minimum_sicaklik, 2)
print(f"Maksimum Sıcaklık: {maksimum_sicaklik}°C")
print(f"Minimum Sıcaklık: {minimum_sicaklik}°C")
print(f"Sıcaklık Farkı: {sicaklik_farki}°C")

print("\n--- Ortalama Sıcaklık ---")
ortalama_sicaklik = round(sum(sicakliklar) / len(sicakliklar), 2)
print(f"Ortalama Sıcaklık: {ortalama_sicaklik}°C")