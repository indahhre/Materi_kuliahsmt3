# Definisi kelas User sebagai kelas dasar
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

# Definisi kelas PremiumUser, turunan dari User
class PremiumUser(User):
    def viewProduct(self):
        print(f"{self.username} melihat produk.")

    def addToCart(self):
        print(f"{self.username} menambahkan produk ke keranjang belanja.")

    def applyVoucher(self):
        print(f"{self.username} menerapkan voucher.")

    def requestPrioritySupport(self):
        print(f"{self.username} meminta dukungan prioritas.")

# Definisi kelas Seller, turunan dari User
class Seller(User):
    def addProduct(self):
        print(f"{self.username} menambahkan produk baru ke daftar jual.")

    def processOrder(self):
        print(f"{self.username} memproses pesanan.")

# Membuat objek PremiumUser dan Seller
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)
seller = Seller("sellerPro", "seller@example.com", 202)

# Memanggil metode pada objek PremiumUser
premium_user.viewProduct()
premium_user.addToCart()
premium_user.applyVoucher()
premium_user.requestPrioritySupport()

# Memanggil metode pada objek Seller
seller.addProduct()
seller.processOrder()
