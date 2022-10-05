total, tunai = int(input("Total : ")), int(input("Uang Tunai: "))
kembalian = tunai - total
uang = [100000, 50000, 20000, 10000, 5000, 1000]

#perulangan untuk mencari sisa kembalian
#kondisi jika total lebih kecil dari tunai
if total < tunai:
    for i in uang:
        #program untuk mencari kembalian yang ada di perulangan list uang
        bagi = kembalian // i
        print ("%d uang Rp %d" % (bagi, i)) 
        #program agar bagi bulat yang di variabel bagi tidak mengulang lagi saat kembaliannya sudah dibagi bulat
        kembalian -= bagi * i
#kondisi jika total lebih besar dari tunai
elif total > tunai:
    print("mengutang")
#kondisi jika total sama dengan tunai
else:
    print("uang pas")

#uang : [100000, 50000, 20000, 10000, 5000, 1000]
#perulangan pertama : 
#total<tunai
#100000 < 101000
#bagi = 1000 // 100000 : 0
# 0 uang Rp 100000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 0 * 100000
# 1000 = 1000 - 0
# 1000 = 1000

#perulangan kedua :
#bagi = 1000 // 50000 : 0
# 0 uang Rp 50000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 0 * 50000
# 1000 = 1000 - 0
# 1000 = 1000

#perulangan ketiga :
#bagi = 1000 // 20000 : 0
# 0 uang Rp 20000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 0 * 20000
# 1000 = 1000 - 0
# 1000 = 1000

#perulangan keempat :
#bagi = 1000 // 10000 : 0
# 0 uang Rp 10000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 0 * 10000
# 1000 = 1000 - 0
# 1000 = 1000

#perulangan kelima :
#bagi = 1000 // 5000 : 0
# 0 uang Rp 5000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 0 * 5000
# 1000 = 1000 - 0
# 1000 = 1000

#perulangan keenam : 
#bagi = 1000 // 1000 : 1
# 1 uang Rp 1000
# kembalian = kembalian-bagi * i
# 1000 = 1000 - 1 * 1000
# 1000 = 1000 - 1000
# 1000 = 0
