def hitung_kata(kalimat):
    kalimat = kalimat.strip()
    if kalimat:
        kata_kalimat = kalimat.split()
        jumlah_kata = len(kata_kalimat)
        return jumlah_kata
    else:
        return 0

def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    
    panjang_kalimat = len(kalimat)
    
    jumlah_kata = hitung_kata(kalimat)
    
    print(f"Panjang kalimat: {panjang_kalimat} karakter")
    print(f"Jumlah kata: {jumlah_kata}")

if __name__ == "__main__":
    main()
