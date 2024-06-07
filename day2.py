class Car:
    def __init__(self, merk, model, tahun, odometer):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = odometer

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")

    def gantioli(self):
        print(f"Mobil {self.merk} ini perlu ganti oli ketika odometer {self.odometer}")


class ElectricCar(Car):
    def __init__(self, merk, model, tahun, odometer, baterai):
        super().__init__(merk, model, tahun, odometer)
        self.baterai = baterai

    def daya(self):
        print(f"Mobil ini memiliki daya {self.baterai} -kWh")

    def gantioli(self):
        print(f"Mobil listrik tidak memerlukan ganti oli")


fortunerku = Car('toyota', 'fortuner', 2022, 100000)
print(fortunerku.gantioli())

teslaku = ElectricCar('tesla', 'model X', 2022, 10000, 7500)
print(teslaku.gantioli())