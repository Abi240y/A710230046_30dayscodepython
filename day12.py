# TIKET PESAWAT 
harga_tiket = {
    'Ekonomi': 1000000,
    'Bisnis': 2000000,
    'First Class': 3000000
}

def pesan_tiket():
    print("Selamat datang di Layanan Pemesanan Tiket Pesawat!")
    print("Silakan pilih kelas tiket:")
    print("1. Ekonomi")
    print("2. Bisnis")
    print("3. First Class")

    while True:
        pilihan = input("Masukkan nomor pilihan Anda (1/2/3): ")

        if pilihan == '1':
            kelas = 'Ekonomi'
            break
        elif pilihan == '2':
            kelas = 'Bisnis'
            break
        elif pilihan == '3':
            kelas = 'First Class'
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor 1, 2, atau 3.")

    jumlah_tiket = int(input(f"Berapa tiket {kelas} yang ingin Anda pesan? "))
    total_harga = jumlah_tiket * harga_tiket[kelas]

    print(f"\nTerima kasih! Berikut rincian pesanan Anda:")
    print(f"Kelas: {kelas}")
    print(f"Jumlah Tiket: {jumlah_tiket}")
    print(f"Total Harga: Rp {total_harga:,}")

if __name__ == "__main__":
    pesan_tiket()
