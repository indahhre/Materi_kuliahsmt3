# Kelas dasar User
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def display_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")


# Kelas turunan Seller dari User
class Seller(User):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self.products = {}  # Menyimpan produk dalam bentuk dictionary

    def addProduct(self, product_name, description, price, stock):
        product_id = len(self.products) + 1  # ID produk otomatis
        self.products[product_id] = {
            'name': product_name,
            'description': description,
            'price': price,
            'stock': stock
        }
        print(f"Product '{product_name}' added successfully.")

    def processOrder(self, order_id, status):
        # Proses status pesanan (dalam aplikasi nyata, ini akan lebih kompleks)
        print(f"Order ID {order_id} status updated to '{status}'.")


# Kelas turunan Admin dari User
class Admin(User):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self.user_list = []  # Menyimpan daftar ID pengguna

    def removeUser(self, user_id):
        # Hapus pengguna dari sistem (dalam aplikasi nyata, perlu validasi tambahan)
        if user_id in self.user_list:
            self.user_list.remove(user_id)
            print(f"User ID {user_id} removed from the system.")
        else:
            print(f"User ID {user_id} not found in the system.")

    def generateReport(self, report_type, start_date, end_date):
        # Logika menghasilkan laporan berdasarkan tipe
        if report_type == "transaksi":
            print(f"Generating transaction report from {start_date} to {end_date}.")
        elif report_type == "pengguna":
            print(f"Generating user report from {start_date} to {end_date}.")
        else:
            print("Invalid report type specified.")

# Membuat instance Seller dan Admin
seller1 = Seller(user_id=1, username="seller_123", email="seller@example.com")
admin1 = Admin(user_id=2, username="admin_001", email="admin@example.com")

# Memanggil metode display_info untuk menampilkan informasi pengguna
print("=== Seller Info ===")
seller1.display_info()

print("\n=== Admin Info ===")
admin1.display_info()

# Menambahkan produk baru oleh Seller
print("\n=== Menambahkan Produk ===")
seller1.addProduct(product_name="Laptop", description="Laptop gaming dengan spesifikasi tinggi", price=15000000, stock=5)
seller1.addProduct(product_name="Smartphone", description="Smartphone terbaru dengan kamera terbaik", price=7000000, stock=10)

# Memproses pesanan oleh Seller
print("\n=== Memproses Pesanan ===")
seller1.processOrder(order_id=101, status="dalam pengiriman")
seller1.processOrder(order_id=102, status="selesai")

# Menghapus pengguna oleh Admin
print("\n=== Menghapus Pengguna ===")
admin1.user_list = [1, 2, 3]  # Menambahkan beberapa ID pengguna ke dalam daftar
admin1.removeUser(user_id=3)
admin1.removeUser(user_id=4)  # Menghapus ID yang tidak ada untuk melihat respons

# Menghasilkan laporan oleh Admin
print("\n=== Menghasilkan Laporan ===")
admin1.generateReport(report_type="transaksi", start_date="2023-01-01", end_date="2023-12-31")
admin1.generateReport(report_type="pengguna", start_date="2023-01-01", end_date="2023-12-31")
admin1.generateReport(report_type="invalid", start_date="2023-01-01", end_date="2023-12-31")  # Laporan tipe salah
