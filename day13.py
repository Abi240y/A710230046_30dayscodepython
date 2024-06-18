class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}, umur: {self.umur}")

person1 = Person("Destyan", 19)

person1.display_info()

person1.age = 20

person1.display_info()
