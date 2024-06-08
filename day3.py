class Kucing():
    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur


class Pemilik():
    def __init__(self,nama,alamat, kucing):
        self.nama = nama
        self.alamat = alamat
        self.kucing = kucing

    def tampil(self):
        print(f"Halo, aku {self.nama} berasal dari {self.alamat}")
        print(f"Kucingku berjenis {self.kucing.ras} dengan umur {self.kucing.umur} bulan")


abiyyu = Pemilik(
    nama = "Abiyyu",
    alamat = "Ngawi",
    kucing = Kucing(
        ras = "Anggora",
        umur = 7
        )
)

abiyyu.tampil()