# Membuat Program Paradigma  OOP
class luas:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas_Persegipanjang(self):
        return self.panjang * self.lebar
cek_luas = luas(5,10)

print (f"luas persegi adalah {cek_luas.luas_Persegipanjang()}")