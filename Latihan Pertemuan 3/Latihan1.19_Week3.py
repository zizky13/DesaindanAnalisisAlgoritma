import pandas as pd

mahasiswa = pd.DataFrame([
    ['1','Informatika','50','30','20'],
    ['2','Sistem Informasi','55','30','25'],
    ['3','Teknik Sipil','40','30','10']])

mahasiswa.columns = ['No', 'Prodi', 'Mahasiswa', 'Laki-laki', 'Perempuan']

print(mahasiswa)