def konversi_desimal_ke_biner(desimal):
    if desimal == 0:
        return "0"
    biner = ""
    while desimal > 0:
        sisa = desimal % 2
        biner = str(sisa) + biner
        desimal = desimal // 2
    return biner

bilangan_desimal = int(input("Masukkan bilangan desimal (basis 10): "))

hasil_konversi = konversi_desimal_ke_biner(bilangan_desimal)

print(f"Bilangan biner dari {bilangan_desimal} adalah {hasil_konversi}")
