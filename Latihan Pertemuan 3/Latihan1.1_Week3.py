import datetime

#list = array, hanya saja dalam list tipe data tidak harus semua sama
#buat list mahasiswa
waktu = datetime.datetime.now()
mahasiswa = ["Zikar Nurizky", "2022071048", "Informatika", "Desain dan Analisis Algoritma", waktu, "Universitas Pembangunan Jaya"]
print(mahasiswa[1])
print(mahasiswa[1:2])


# #slicing merupakan teknik mengambil beberapa data dari list dengan range tertentu
# bin_colors = ['Red', 'Green', 'Blue', 'Yellow']
# #disini range nilai yang akan diprint adalah dari index 0 hingga index 1
# for i in bin_colors:
#     print("Square " + i)

#for loop
for i in mahasiswa:
    print("UPJ " + str(i))