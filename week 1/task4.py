def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cikar(sayi1, sayi2):
    return sayi1 - sayi2

def carp(sayi1, sayi2):
    return sayi1 * sayi2

def bol(sayi1, sayi2):
    if sayi2 == 0:
        print("Geçersiz işlem! Sıfıra bölünemez!")
        return None
    else:
        return sayi1 / sayi2

def hesaplamalari_yazdir(sayi1, sayi2):
    print("Toplama: ", topla(sayi1, sayi2))
    print("Çıkarma: ", cikar(sayi1, sayi2))
    print("Çarpma: ", carp(sayi1, sayi2))
    bolme_sonucu = round(bol(sayi1, sayi2), 2)
    print("Bölme: ", bolme_sonucu)


sayi_1 = int(input("Lütfen birinci sayıyı girin: \n"))
sayi_2 = int(input("Lütfen ikinci sayıyı girin: \n"))

hesaplamalari_yazdir(sayi_1, sayi_2)