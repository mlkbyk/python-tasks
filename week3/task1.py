import math

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

try:
    n_input = int(input("Fibonacci serisi uzunluğu (n) girin: "))
    
    # Generator'dan çekilen sayıları filtrele (çift olanlar) ve karekökünü al
    sonuc = list(map(lambda x: round(math.sqrt(x), 2), 
                     filter(lambda x: x % 2 == 0, fibonacci_generator(n_input))))
    
    print(f"Sonuç: {sonuc}")
except ValueError:
    print("Lütfen geçerli bir tamsayı girin.")
