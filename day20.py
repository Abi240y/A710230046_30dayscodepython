#program diskon tiket

tahunlahir = input("masukan tahun lahir : ")
umur = int(2023) - int(tahunlahir)
hargatiketdasar = 200000
if (umur>=0 and umur<5):
    hargadiskon = hargatiketdasar * (100/100)
    hargatiketsaatini = hargatiketdasar - hargadiskon
    print("inilah harga setelah diskon",hargatiketsaatini)
elif (umur >=5 and umur<11):
    hargadiskoon = hargatiketdasar * (50/100)
    hargatiketsekarang = hargatiketdasar - hargadiskoon
    print("inilah harga setelah diskon",hargatiketsekarang)    

else :
    print("harga tiket",hargatiketdasar)