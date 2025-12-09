import math
import functools

def istatistik_stream():
    window = []
    result = None
    while True:
        # Veriyi al
        val = yield result
        if val is None: continue
            
        window.append(val)
        # Sadece son 5 veriyi tut
        if len(window) > 5:
            window.pop(0)
            
        # İstatistikleri hesapla
        avg = functools.reduce(lambda a, b: a+b, window) / len(window)
        
        # Standart sapma (Lambda ile)
        variance = sum(map(lambda x: (x - avg) ** 2, window)) / len(window)
        std_dev = math.sqrt(variance)
        
        # Anomaly Detection (3 sigma kuralı)
        # Standart sapma 0 ise anomali yoktur
        is_anomaly = abs(val - avg) > (3 * std_dev) if std_dev > 0 else False
        
        result = {"mean": avg, "std": std_dev, "anomaly": is_anomaly}

# Sistemi başlat
stream = istatistik_stream()
next(stream) # Generator'ı hazırla

print("Sayı giriniz (Çıkış için 'quit' yazın):")
while True:
    user_in = input("> ")
    if user_in.lower() == 'quit':
        break
    try:
        sayi = float(user_in)
        stats = stream.send(sayi)
        
        durum = "ANOMALİ TESPİT EDİLDİ!" if stats['anomaly'] else "Normal"
        print(f"Ort: {stats['mean']:.2f}, Std: {stats['std']:.2f}, Durum: {durum}")
        
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")
