#Membuat Class
class mobil :
      Jumlah_mobil = 0
      # Membuat Construktor
      def __init__(self, ban, merk, cc):
          # Instance Variabel
          self.merkban = ban
          self.merkmobil = merk
          self.kapasitas = cc
          mobil.Jumlah_mobil += 1
     #Membuat Method String 
      def __str__(self):
           return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
      #Membuat Method Baru Bore up
      def boreup(self, bore):
           self.kapasitas += bore
           
#Membuat Objek Baru M1
M1 = mobil("Brigestone", "Toyota-Kijang", 1500)
print(M1)
print("Jumlah Mobil:", mobil.Jumlah_mobil)
M1.boreup(500)
print(M1)
#Membuat Objek Baru M2
M2 = mobil("Pirelli", "Subaru", 2000)
print(M2)
print("Jumlah Mobil:", mobil.Jumlah_mobil)