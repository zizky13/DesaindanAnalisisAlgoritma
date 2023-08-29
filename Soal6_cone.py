# Algoritma:
# Tahap 1: Tentukan nilai diameter = 5 dan tinggi = 4
# Tahap 2: Hitung nilai jari-jari dengan membagi dua nilai diameter r = d/2, lanjut ke tahap 3
# Tahap 3: Hitung luas menggunakan nilai jari-jari dan tinggi dengan cara memasukan nilai ke rumus = 3.14 * 0.33 * r * r * t
# Tahap 4: Kembalikan hasil hitung luas
#
# Psuedocode:
# r = 3
# d = r / 2
# t = 5
# luas = 3.14 * 0.33 * r * r * t
# return luas

d = 5
t = 4
r = d / 2
luas = 3.14 * 0.33 * r * r * t
print(luas)