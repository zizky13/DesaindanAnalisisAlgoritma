# Algoritma:
#
# Tahap 1: Cek apakah piring 1 berisi pisang dan piring 2 berisi manggis? Jika ya, maka program selesai. Jika tidak, lanjut ke tahap 2
# Tahap 2: Pindahkan pisang dari piring 2 ke piring 3
# Tahap 3: Pindahkan manggis dari piring 1 ke piring 2
# Tahap 4: Pindahkan pisang dari piring 3 ke piring 1
# Tahap 5: Kembali ke tahap 1
#
# Psuedocode:
#
# while (p1 != pisang and p2 != manggis)
#     p3 -> pisang
#     p2 -> manggis
#     p1 -> p3
# return p1 and p2

p1 = "manggis"
p2 = "pisang"
p3 = ""

while (p1 != "pisang" and p2 != "manggis"):
    p3 = p2
    p2 = p1
    p1 = p3

print(p1, p2)