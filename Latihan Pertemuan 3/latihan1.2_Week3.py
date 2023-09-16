#tuples is similar to list
#the only difference is tuples is read-only file

# UPJ = ('Universitas', 'Pembangunan', 'Jaya')
# print(UPJ[0:])

#Example of nested tuples
hariAwal = ("Senin", "Selasa", "Rabu")
hariAkhir = ("Kamis", "Jumat", "Sabtu")

#dua tuples bisa digabung menjadi satu tuples, concatenate
hari = (hariAwal, hariAkhir)
print(hari)

#Exercise of nested tuples
pertama = (100)
kedua = (200, 400, 600)
ketiga = (300)
keempat = (400,800)
nested_tuple = (pertama, kedua, ketiga, keempat)
print(nested_tuple)