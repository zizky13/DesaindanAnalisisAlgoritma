# Mencari pasangan titik jarak terdekat

from math import sqrt
from random import randint
titik = []
n = int(input('Masukkan jumlah titik yang Anda cari jaraknya: '))
for i in range (0, n):
    titik.append([randint(0, 100), randint(0, 100)])
print('Titik:\n', titik)

def hitungjarak(lis):
    lisjarak = []
    for i in range (0, len(lis)-1):
        for j in range ( i+1, len(lis)):
            jarak = sqrt((lis[i][0]-lis[j][0])**2 + (lis[i][1] - lis[j][1])**2)
            lisjarak.append(jarak)
            print('Titik: ', lis[i], 'Titik: ', lis[j], ': ', jarak)
    return min(lisjarak)
print('Jarak terdekat:\n', hitungjarak(titik))