# Örnek veri
veri = [1, [2, [3, 4]], 5, [6, 'a'], 'b', 7]

# Recursive lambda ile listeyi düzleştirme
flatten = lambda l: sum(map(flatten, l), []) if isinstance(l, list) else [l]

# Map/Filter ile sadece sayıları (int, float) koruma
temiz_liste = list(filter(lambda x: isinstance(x, (int, float)), flatten(veri)))

print(f"Orijinal: {veri}")
print(f"İşlenmiş: {temiz_liste}")
