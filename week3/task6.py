# Kullanıcıdan girdi al
girdi = input("İsimleri virgülle ayırarak girin (örn: ali, ayşe): ")

# Lambda ve map ile işleme
formatli_isimler = list(map(lambda x: f"Sayın {x.strip().upper()}", girdi.split(',')))

print(formatli_isimler)
