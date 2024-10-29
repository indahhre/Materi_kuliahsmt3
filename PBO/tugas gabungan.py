# Kelas Dasar
class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies

    def info(self):
        return f"Nama: {self.nama}, Spesies: {self.spesies}"

# Kelas Turunan Pertama
class Kelinci(Hewan):
    def __init__(self, nama, umur):
        super().__init__(nama, "Kelinci")
        self.umur = umur

    def melompat(self):
        return f"{self.nama} sedang melompat!"

    def info_kelinci(self):
        return f"{self.info()}, Umur: {self.umur} tahun"

# Kelas Turunan Kedua
class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")
        self.ras = ras

    def menggonggong(self):
        return f"{self.nama} berkata: Guk Guk!"

    def info_anjing(self):
        return f"{self.info()}, Ras: {self.ras}"

# Membuat Objek
kelinci = Kelinci("Lola", 2)
anjing = Anjing("Buddy", "Golden Retriever")

# Menggunakan Metode dari Kelinci
print(kelinci.info_kelinci())
print(kelinci.melompat())

# Menggunakan Metode dari Anjing
print(anjing.info_anjing())
print(anjing.menggonggong())
