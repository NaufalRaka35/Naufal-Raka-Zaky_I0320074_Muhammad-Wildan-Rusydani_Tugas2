# biodata
nama = "Naufal Raka Zaky"
nim = "I0320074"
jenis_kelamin = "Laki-laki"
prodi = "Teknik Industri UNS"
angkatan = 2020
tempat_lahir = "Boyolali"
tg_lahir = "25 September 2001"

# umur
tgl_lahir = 4
bln_lahir = 7
thn_lahir = 2002
lahir = tgl_lahir+(bln_lahir*30)+(thn_lahir*365)
tsekarang = 11
bsekarang = 3
ysekarang = 2021
sekarang = tsekarang+(bsekarang*30)+(ysekarang*365)
tahun = int((sekarang-lahir)/365)
bulan = int(((sekarang-lahir)%365)/30)
hari = int(((sekarang-lahir)%365)%30)

# alamat dan lingkungan tempat tinggal
alamat = "Tanduk, RT03 RW01, Ampel, Boyolali."
lingkungan = "Rumah saya berada di desa dengan lingkungan yang asri dan hijau karena jauh dari perkotaan"

# informasi tambahan
bb = 77
tb = 176
uk_sepatu = 43
makanan_fav = "Pisang goreng"
minuman_fav = "Es lemon tea"
hobi = "Olahraga dan nongkrong."

# tampilkan semua informasi di layar
print("Nama :",nama)
print("NIM  :",nim)
print("Jenis kelamin :",jenis_kelamin)
print("Alamat :",alamat)
print("Saya merupakan seorang mahasiswa",prodi,"angkatan",angkatan)
print("Saya lahir di",tempat_lahir,"pada tanggal",tg_lahir,"dan sekarang berumur",tahun,"tahun",bulan,"bulan",hari,"hari")
print(lingkungan)
print("Hobi saya adalah",hobi)
print("Berat badan saya",bb,"kg, serta","tinggi saya",tb,"cm")
print("Ukuran sepatu saya yaitu",uk_sepatu)
print("Makanan favorit saya",makanan_fav,"dan minuman favorit saya yaitu",minuman_fav)

