#Program jika 1 hari = 360 derajat

x = float(input("Derajat : "))
t = x*24*3600/360+6*3600

jam = t // 3600
sisa_detik = t - 3600 * jam
menit = sisa_detik // 60
detik = sisa_detik - (60 * menit)

if jam >= 24:
    jam = jam % 24

if jam >= 00 and jam <5:
    print ("Selamat Dini Hari")

elif jam >= 5 and jam <= 10:
    print ("Selamat Pagi")

elif jam >= 10 and jam <= 14:
    print ("Selamat Siang")

elif jam >= 15 and jam <= 18:
    print ("Selamat Sore")

elif jam >= 18 and jam <= 00:
    print ("Selamat Malam")

print("%02d:%02d:%02d" % (jam,menit,detik))