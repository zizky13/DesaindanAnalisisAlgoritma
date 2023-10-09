def hitung_faktorial(n):
    if n > 2:
        return n * hitung_faktorial(n - 1)

    return 2

n = int(input("Masukkan nilai n: "))
faktorial = hitung_faktorial(n)
print(f"{n}! = {faktorial}")