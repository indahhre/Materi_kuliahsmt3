# Kelas Dasar
class Laptop:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Merek: {self.merk}, Tahun: {self.tahun}"

# Kelas Turunan Pertama
class GamingLaptop(Laptop):
    def __init__(self, merk, tahun, kartu_grafis):
        super().__init__(merk, tahun)
        self.kartu_grafis = kartu_grafis

    def info_gaming(self):
        return f"{self.info()}, Kartu Grafis: {self.kartu_grafis}"

    def bermain_game(self):
        return f"{self.merk} siap untuk bermain game."

# Kelas Turunan Kedua
class Ultrabook(Laptop):
    def __init__(self, merk, tahun, berat):
        super().__init__(merk, tahun)
        self.berat = berat

    def info_ultrabook(self):
        return f"{self.info()}, Berat: {self.berat} kg"

    def produktivitas(self):
        return f"{self.merk} cocok untuk produktivitas sehari-hari."

# Kelas Turunan Kedua dari GamingLaptop
class LaptopGamingPremium(GamingLaptop):
    def __init__(self, merk, tahun, kartu_grafis, layar):
        super().__init__(merk, tahun, kartu_grafis)
        self.layar = layar

    def info_laptop_premium(self):
        return f"{self.info_gaming()}, Layar: {self.layar} inci"

    def raytracing(self):
        return f"{self.merk} mendukung teknologi ray tracing."

# Kelas Turunan Kedua dari Ultrabook
class UltrabookRingan(Ultrabook):
    def __init__(self, merk, tahun, berat, daya_tahan_baterai):
        super().__init__(merk, tahun, berat)
        self.daya_tahan_baterai = daya_tahan_baterai

    def info_ultrabook_ringan(self):
        return f"{self.info_ultrabook()}, Daya Tahan Baterai: {self.daya_tahan_baterai} jam"

    def bawa_perjalanan(self):
        return f"{self.merk} sangat ringan untuk dibawa bepergian."

# Contoh Penggunaan
gaming_laptop = LaptopGamingPremium("ASUS ROG", 2023, "NVIDIA RTX 3060", 15.6)
print(gaming_laptop.info_laptop_premium())
print(gaming_laptop.bermain_game())
print(gaming_laptop.raytracing())

ultrabook = UltrabookRingan("Dell XPS", 2022, 1.2, 12)
print(ultrabook.info_ultrabook_ringan())
print(ultrabook.produktivitas())
print(ultrabook.bawa_perjalanan())

