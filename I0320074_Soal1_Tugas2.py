print("== Menghitung Luas Persegi Panjang ==")
panjang = float(input("Memasukkan panjang :"))
lebar = float(input("Memasukkan lebar :"))
luas = (panjang*lebar)
print("Luas dari persegi panjang :",luas,"satuan")

print("== Menghitung Luas Lingkaran ==")
phi = 3.14
jari_jari = float(input("Memasukkan jari-jari :"))
luas = jari_jari*jari_jari*phi
print("Luas lingkaran :",luas,"satuan")

print("== Menghitung Luas Kubus ==")
sisi = float(input("Memasukkan sisi kubus:"))
luas_permukaan = 6*sisi*sisi
print("Luas permukaan kubus :",luas_permukaan,"satuan")

print("== Menghitung Konversi Suhu dari Celcius ke Fahrenheit ==")
celcius = float(input("Memasukkan suhu celcius :"))
konversi = (((9/5)*celcius)+32)
print("Mengonversi suhu dari celcius ke fahrenheit :",konversi,"derajat")

print("Menghitung konversi suhu dari Reamur ke Kelvin")
reamur = float(input("Memasukkan suhu reamur :"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu dari reamur ke kelvin adalah",konversi,"derajat")