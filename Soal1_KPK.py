# Algoritma:
# Tahap 1: Tentukan nilai A = 3 dan B = 4
# Tahap 2: Jika sisa hasil bagi nilai pertama dan nilai kedua sama dengan nol, kembalikan nilai pertama sebagai KPK. Jika tidak, lanjut ke tahap kedua
# Tahap 3: Jika nilai pertama lebih kecil dari nilai kedua, tambahkan nilai pertama sebanyak nilai awal nilai pertama
# Tahap 4: Jika nilai pertama lebih besar dari nilai kedua, tambahkan nilai kedua sebanyak nilai awal nilai kedua
# Tahap 5: Kembali ke tahap 1
#
# Psuedocode:
# A = 3
# B = 4
# while (A % B != 0):
#     A = A + 3
# return A

A = 3
B = 4
while (A % B != 0):
    A = A + 3
print(A)

