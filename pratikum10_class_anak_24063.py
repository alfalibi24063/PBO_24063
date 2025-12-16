class Parent:
    pass

class Child(Parent):
    pass

class Hewan:
    def mandi(self):
        print("Hewan sedang mandi")

class burung(Hewan):
    def suara(self):
        print("burung")

k = burung()
k.mandi()
k.suara()


class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Motor(Kendaraan):
    def jalan(self):
        print("Motor sedang berhenti")

m = Motor("KAWASAKI")
m.info()
m.jalan()

class manusia:
    def suara(self):
        print("Suara manusia")

class manusia(manusia):
    def suara(self):
        print("HALOH DEK")

a = manusia()
a.suara()

class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

class pesawat(Kendaraan):
    def __init__(self, merk, warna):
        super().__init__(merk)
        self.warna = warna

m = pesawat("HONDA", "putih")
print(m.merk)
print(m.warna)

class info3:
    def metodeA(self):
        print("Ini dari class info3")

class info4:
    def metodeB(self):
        print("Ini dari class info4")

class C(info3, info4):
    pass

obj = C()
obj.metodeA()
obj.metodeB()



