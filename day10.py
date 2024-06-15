def cek_prima(n):
    """ Fungsi untuk memeriksa apakah suatu bilangan n adalah bilangan prima """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    
    return True

def cari_bilangan_prima(dari, sampai):
    """ Fungsi untuk mencari bilangan prima dalam rentang dari sampai """
    bilangan_prima = []
    for angka in range(dari, sampai + 1):
        if cek_prima(angka):
            bilangan_prima.append(angka)
    return bilangan_prima

batas_bawah = 1
batas_atas = 50
prima_dalam_rentang = cari_bilangan_prima(batas_bawah, batas_atas)
print(f"Bilangan prima antara {batas_bawah} dan {batas_atas} adalah:")
print(prima_dalam_rentang)
