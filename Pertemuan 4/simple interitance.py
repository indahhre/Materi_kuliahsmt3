# Membuat sebuah Super Class
class animal:
    #Membuat kontruktor untuk menampung attribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras
#membuat method bersuara
def Speaks(self):
      print (f"{self.name} bisa bersuara")
#membuat kelas 1 turunan dari super kelas
class Cat(animal):
    def speaksCat(self):
        print(f"nama{self.name} dengan ras {self.ras} bersuara Meooooowww")    
# membuat kelas 2 turunan dari super kelas
class Dog(animal):
    def speaksDog(self):
        print(f"nama {self.name} dariras {self.ras} Bersuara guk guk")
# Membuat objek
cat = Cat ("kitty", "angora")
cat.speaksCat()
Dog = Dog("puppy", "pitbull")
Dog.speaksDog()