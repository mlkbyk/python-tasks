islemler = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

print("İşlemler: +, -, *, /")
secim = input("İşlemi seçin: ")

try:
    if secim not in islemler:
        print("Geçersiz işlem tipi girdiniz.")
    else:
        s1 = float(input("Birinci sayı: "))
        s2 = float(input("İkinci sayı: "))
        
        sonuc = islemler[secim](s1, s2)
        print(f"Sonuç: {sonuc}")
        
except ZeroDivisionError:
    print("Hata: Bir sayı sıfıra bölünemez.")
except ValueError:
    print("Hata: Lütfen sayısal değerler girin.")
