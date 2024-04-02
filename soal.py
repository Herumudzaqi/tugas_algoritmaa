print('SELEKSI PENERIMAAN PEKERJAAN')
listpendidikan = ['smk','sma','diploma','sarjana']
listpengalaman = ['1 tahun', '2 tahun', '3 tahun']
nama = str(input('Masukan Nama : '))
umur = int(input('Masukan Umur : '))
pendidikan = str(input('Masukan Pendidikan [min.sma] : '))
kesehatan = str(input('Masukan Kesehatan [sehat/tidak] : '))
pengalaman = str(input('Masukan Pengalaman : '))
kriteria = nama,umur,pendidikan,kesehatan,pengalaman
if umur >= 18 and pendidikan in listpendidikan and kesehatan == 'sehat' and pengalaman in listpengalaman : 
    print('selamat anda diterima')
    print('anda dinyalankan lolos seleksi')
else : 
    print('coba lagi lain waktu')
print(kriteria)