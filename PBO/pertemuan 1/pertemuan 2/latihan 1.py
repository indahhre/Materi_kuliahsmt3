#Membuat Perpustakaan
class Buku :
      Jumlah_buku = 0
      # Membuat Construktor
      def __init__(self, judul, penulis, tahun):
          # Instance Variabel
          self.judul = judul
          self.penulis = penulis
          self.tahun = tahun
          Buku.Jumlah_buku += 1
     #Membuat Method String 
      def __str__(self):
           return f"{self.judul}, {self.penulis}, {self.tahun}"
      #Membuat Method Baru Bore up
      def boreup(self, bore):
           self.tahun += bore
           
#Membuat Objek Baru M1
B1 = Buku("Abighea", "Chelsea Karina", 2021)
print(B1)
print("Jumlah buku:", Buku.Jumlah_buku)
B1.boreup(500)
print(B1)
#Membuat Objek Baru M2
B2 = Buku("Rindu", "Tere Liye", 2014)
print(B2)
print("Jumlah buku:", Buku.Jumlah_buku)