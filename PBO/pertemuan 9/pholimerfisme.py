# Tanpa Implementasi Polimerfisme
class jumlah:
    def tambah1(n1, n2):
        print(f"Hasilnya  {n1+n2}")
objek3 = jumlah
objek3.tambah1(1,2)
    
# implementasi polimerfisme
class penjumlahan:
    def  tambah(*num):
        return sum(num)
objek1 = penjumlahan
print(objek1.tambah(2,3,5,10))
    
#mengggunakan default paramenter
class default:
    def tambah2( a, b=0,c=0,d=0,e=0):
        print (f"hasilnya {a+b+c+d+e}")
objek2 = default
objek2.tambah2(2,4,2,3,5)