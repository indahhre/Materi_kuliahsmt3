# implementasi polimerfisme dengan bangun datar
class BangunDatar:  #abstract Class
    def luas(self): #abstarct method
        raise NotImplementedError("Menthod ini wajib diimplementasikan")
class Persegi(BangunDatar): #kelas turunan 1
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        print(f"Luas Persegi Adalah: {self.sisi**2}")
class segitiga(BangunDatar): #kelas turunan 2
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        print(f"Luas Segitiga adalah: {(self.alas*self.tinggi)/2}")
class Lingkaran(BangunDatar): #kelas turunan 3
    def __init__(self, r, pi=3.14):
        self.pi = pi
        self.r = r
    def luas(self):
        print(f"Luas segitiga adalah: {self.pi*self.r**2}")

objek1 = Persegi(2)
objek2 =  segitiga(2,3)
objek3 = Lingkaran(5)
objek1.luas()
objek2.luas()
objek3.luas()