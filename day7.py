class Hewan:
    def bersuara(self):
        print("Sebuah hewan mengeluarkan suara")

class Anjing(Hewan):
    def bersuara(self):
        print("Guk!")

class Kucing(Hewan):
    def bersuara(self):
        print("Meong!")

class Bebek(Hewan):
    def bersuara(self):
        print("Kwek!")

# Fungsi untuk membuat hewan-hewan berbicara
def hewan_bicara(hewan):
    hewan.bersuara()

# Membuat instansi dari hewan-hewan yang berbeda
anjing = Anjing()
kucing = Kucing()
bebek = Bebek()

# Memanggil fungsi untuk membuat hewan-hewan berbicara
hewan_bicara(anjing)   # Output: Guk!
hewan_bicara(kucing)   # Output: Meong!
hewan_bicara(bebek)    # Output: Kwek!
