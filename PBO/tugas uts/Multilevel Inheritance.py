class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna '{self.username}' dengan email '{self.email}' berhasil login.")

    def logout(self):
        print(f"Pengguna '{self.username}' berhasil logout.")


# Contoh penggunaan kelas User
user = User("Indah_rizkika", "indahre@example.com", "U1001")

# Login dan Logout
user.login()
user.logout()

class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna '{self.username}' dengan email '{self.email}' berhasil login.")

    def logout(self):
        print(f"Pengguna '{self.username}' berhasil logout.")


# Kelas turunan pertama dari User
class BasicUser(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    
    def viewProduct(self, productId):
        # Simulasi menampilkan informasi produk berdasarkan productId
        print(f"{self.username} sedang melihat informasi produk dengan ID: {productId}.")
    
    def addToCart(self, productId, quantity):
        # Simulasi menambahkan produk ke keranjang belanja
        print(f"{self.username} menambahkan produk dengan ID: {productId} sebanyak {quantity} ke keranjang belanja.")


# Contoh penggunaan kelas BasicUser
basic_user = BasicUser("Indah_rizkika", "indahre@example.com", "U1001")

# Login
basic_user.login()

# Melihat produk dan menambahkan ke keranjang belanja
basic_user.viewProduct("P2001")
basic_user.addToCart("P2001", 3)

# Logout
basic_user.logout()

class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna '{self.username}' dengan email '{self.email}' berhasil login.")

    def logout(self):
        print(f"Pengguna '{self.username}' berhasil logout.")


# Kelas turunan pertama dari User
class BasicUser(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    
    def viewProduct(self, productId):
        print(f"{self.username} sedang melihat informasi produk dengan ID: {productId}.")
    
    def addToCart(self, productId, quantity):
        print(f"{self.username} menambahkan produk dengan ID: {productId} sebanyak {quantity} ke keranjang belanja.")


# Kelas turunan kedua dari BasicUser
class PremiumUser(BasicUser):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)

    def applyVoucher(self, voucherCode, cartTotal):
        # Simulasi penerapan voucher diskon
        discount = 0.1  # diskon 10% untuk pengguna premium
        new_total = cartTotal * (1 - discount)
        print(f"Voucher '{voucherCode}' berhasil diterapkan. Total belanja setelah diskon: {new_total:.2f}")

    def requestPrioritySupport(self, issueDescription):
        # Simulasi menghubungi dukungan prioritas
        print(f"Permintaan dukungan prioritas diterima dari {self.username}. Masalah: {issueDescription}")


# Contoh penggunaan kelas PremiumUser
premium_user = PremiumUser("Indah_rizkika", "indahre@example.com", "U1002")

# Login
premium_user.login()

# Melihat produk dan menambahkan ke keranjang belanja
premium_user.viewProduct("P3001")
premium_user.addToCart("P3001", 2)

# Menerapkan voucher dan menghubungi dukungan prioritas
premium_user.applyVoucher("DISC10", 100.0) 
premium_user.requestPrioritySupport("Produk yang dipesan tidak sesuai deskripsi.")

# Logout
premium_user.logout()
