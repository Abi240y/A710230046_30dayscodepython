# Program Kasir Sederhana

def hitung_total(items):
    total = 0
    for item in items:
        total += item[1] * item[2]  
    return total

def cetak_struk(items, total):
    print("=== Struk Pembelian ===")
    for item in items:
        print(f"{item[0]} \t x{item[1]} \t Rp {item[2] * item[1]}")
    print("=======================")
    print(f"Total \t\t Rp {total}")
    print("=======================")


def main():
    items = []
    while True:
        nama_barang = input("Masukkan nama barang (Ketik 'selesai' untuk selesai belanja): ")
        if nama_barang.lower() == 'selesai':
            break
        jumlah = int(input("Masukkan jumlah barang: "))
        harga_satuan = float(input("Masukkan harga satuan: "))
        items.append((nama_barang, jumlah, harga_satuan))

    total_harga = hitung_total(items)
    cetak_struk(items, total_harga)

if __name__ == "__main__":
    main()
