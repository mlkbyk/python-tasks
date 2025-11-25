print("---Kredi Başvuru Sistemi---")
print("Kredi onayı için kurallar:")
print("1. 18 yaşından küçükler kredi alamaz.")
print("2. 18-65 yaş arası ve geliri 5000 TL üzeri olanlar kredi alabilir.")
print("3. 18-65 yaş arası ve geliri 5000 TL veya altı olanlar için gelir yetersiz.")
print("4. 65 yaşından büyükler kredi alamaz.\n")


kullanici_yas = int(input("Lütfen yaşınızı girin: \n"))
kullanici_gelir = float(input("Lütfen aylık gelirinizi girin (TL): \n"))

if kullanici_yas < 18:
    print("18 yaşından küçükler kredi alamaz.")
elif kullanici_yas > 65:
    print("65 yaşından büyükler kredi alamaz.")
else:
    if kullanici_gelir > 5000:
        print("Kredi başvurunuz onaylandı!")
    else:
        print("Maalesef geliriniz yetersiz. Kredi başvurunuz reddedildi.")