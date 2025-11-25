import string

python_metni = "Python, Guido van Rossum tarafından 1991 yılında geliştirilmiş bir programlama dilidir.\
 Python, okunabilirliği ve basit sözdimleri ile öne çıkar. \
 Dilin tasarım felsefesi, kod okunabilirliğini vurgular ve bu da onu yeni başlayanlar için ideal kılar. \
 Python, web geliştirme, veri analizi, yapay zeka, bilimsel hesaplama ve otomasyon gibi birçok alanda kullanılır.\
 Python'un geniş kütüphane ekosistemi, geliştiricilere güçlü araçlar sunar.\
 Python topluluğu çok aktiftir ve sürekli olarak dilin gelişimine katkıda bulunur. \
 Python programlama dilini öğrenmek, yazılım dünyasında birçok kapı açar."

python_metni = python_metni.lower()

temiz_metin = ''.join([c for c in python_metni if c not in string.punctuation])
kelimeler = temiz_metin.split()

kelime_sayilari = {}

for kelime in kelimeler:
    if kelime in kelime_sayilari:
        kelime_sayilari[kelime] += 1
    else:
        kelime_sayilari[kelime] = 1

kelime_sayilari.items()
siralanmis_liste = sorted(kelime_sayilari.items(), key=lambda x: x[1], reverse=True)[:3]

for i in siralanmis_liste:
    print(i)