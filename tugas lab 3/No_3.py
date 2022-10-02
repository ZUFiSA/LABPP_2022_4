from math import floor

harga_barang= int(input("Harga Barang: "))
nilai_uang= int(input("jumlah uang': "))
c = int(nilai_uang-harga_barang)

seratusribu = 0
limapuluhribu = 0
duapuluhribu = 0
sepuluhribu = 0
limaribu = 0
duaribu = 0
seribu = 0

         
if c== 0:
    print("uang pas")

elif c<0:
    print("uang kurang")
else:

    while c >= 100000: 
        d = floor(c/100000)
        seratusribu = seratusribu + d
        c = c%100000
    while c >= 50000:
        d = floor(c/50000)
        limapuluhribu = limapuluhribu + d
        c = c%50000
    while c >= 20000:
        d = floor(c/20000)
        duapuluhribu= duapuluhribu + d
        c = c%20000
    while c >= 10000:
        d = floor(c/10000)
        sepuluhribu = sepuluhribu + d
        c = c%10000
    while c >= 5000:
        d = floor(c/5000)
        limaribu = limaribu + d
        c = c%5000
    while c >= 2000:
        d = floor(c/2000)
        duaribu = duaribu + d
        c = c%2000
    while c >= 1000:
        d = floor(c/1000)
        seribu = seribu + d
        c = c%1000

   
        
    else:
        print(seratusribu,"uang Rp.100.000")
        print(limapuluhribu,"uang Rp.50.000")
        print(duapuluhribu,"uang Rp.20.000")
        print(sepuluhribu,"uang Rp.10.000")
        print(limaribu,"uang Rp.5.000")
        print(duaribu,"uang Rp.2.000")
        print(seribu,"uang Rp.1.000")
       
        
 
   
    