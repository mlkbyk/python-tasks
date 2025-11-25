print("---Giriş ve kayıt sistemine hoş geldiniz---")
print("Lütfen kayıt olmak için kurallara uyun: ")
print("1. Kullanıcı adı en az 3 karakter uzunluğunda olmalıdır.")
print("2. Şifre en az 6 karakter uzunluğunda olmalı ve en az 1 rakam içermelidir.")
print("3. E-posta '@' sembolünü içermelidir.")
print("4. Yaş 13'ten büyük olmalıdır.\n")


kullanici_adi = input("Lütfen kullanıcı adınızı girin: \n")
sifre = input("Lütfen şifrenizi girin: \n")
eposta = input("Lütfen e-posta adresinizi girin: \n")
yas = int(input("Lütfen yaşınızı girin: \n"))


gecerli_kullanici_adi = len(kullanici_adi) >= 3
gecerli_sifre = len(sifre) >= 6 and any(karakter.isdigit() for karakter in sifre)
gecerli_eposta = "@" in eposta
gecerli_yas = yas > 13


if not gecerli_kullanici_adi:
    print("Kullanıcı adı en az 3 karakter olmalı!")
if not gecerli_sifre:
    print("Şifre en az 6 karakter olmalı ve en az 1 rakam içermeli!")
if not gecerli_eposta:
    print("E-posta '@' sembolünü içermeli!")
if not gecerli_yas:
    print("13 yaşından büyük olmalısınız!")


dogrulama = gecerli_kullanici_adi and gecerli_sifre and gecerli_eposta and gecerli_yas


if dogrulama:
    print("\nKayıt başarılı!")
else:
    print("\nGeçersiz durum, lütfen tekrar deneyin.")

print("Doğrulama durumu:", dogrulama)