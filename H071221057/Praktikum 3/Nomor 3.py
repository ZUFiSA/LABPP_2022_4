#Inputan yang dikasih masuk
total, tunai = int(input("Total : ")), int(input("Uang Tunai : "))
#Mencari sisa uang dari barang yang telah kita beli
kembalian = tunai - total
#Daftar lembaran uang kembalian
uang = (100000,50000,20000,10000,5000,1000)
#Perulangan mencari sisa kembalian
if total < tunai:
    for i in uang:
     bagi = kembalian // i
     print("%d uang Rp %d" % (bagi, i))
     kembalian -= bagi * i

elif total == tunai:
    print("0")

else:
    print(" UANGTA BOS NDAK CUKUPKI")

#total 100000
#uangtunai=101000
#kembalian=tunai - total = 101000 - 100000= 1000
 #perulangan 1,i=100000
 #bagi=kembalian // i = 1000 // 100000 = 0
 #0 uang 100k
 #kembalian = kembalian - bagi * i= 1000 - 0 * 100k

 # total 50000
 #perulangan 2, i=50k
 #bagi=kembalian // i = 51000//50000 = 0
 #0 uang 50k
 #kembalian = kembalian - bagi * i= 51000 - 0 * 51000

 


