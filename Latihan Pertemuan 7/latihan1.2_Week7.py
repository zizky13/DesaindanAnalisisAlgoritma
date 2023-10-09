def CariFaktor (n):
    if n <= 1:
        return 1
    else:
        return CariFaktor(n - 1) * n


n = int(input("Masukkan nilai n: "))
print(f"Hasil dari {n}!", CariFaktor(n))