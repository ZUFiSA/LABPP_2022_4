#Menentukan jumlah bilangan genap, ganjil, positif, dan negatif

import sys
genap = 0
ganjil = 0
positif = 0
negatif = 0

bilangan_1, bilangan_2, bilangan_3, bilangan_4, bilangan_5 = input("Masukkan 5 bilangan : ").split(" ")

#Cek angka negatif
if not bilangan_1.isnumeric():
    if bilangan_1[0] == '-' and len(bilangan_1) > 1:
        negatif += 1
    else:
        sys.exit("Inputan tidak valid")

bilangan_1 = int(bilangan_1)

#Cek angka genap dan ganjil
if bilangan_1 % 2 == 0 or bilangan_1 == 0:
    genap += 1
else:
    ganjil += 1

#Cek angka positif
if bilangan_1 > 0:
    positif += 1 

#Cek angka negatif
if not bilangan_2.isnumeric():
    if bilangan_2[0] == '-' and len(bilangan_2) > 1:
        negatif += 1
    else:
        sys.exit("Inputan tidak valid")

bilangan_2 = int(bilangan_2)

#Cek angka genap dan ganjil
if bilangan_2 % 2 == 0 or bilangan_2 == 0:
    genap += 1
else:
    ganjil += 1

#Cek angka positif
if bilangan_2 > 0:
    positif += 1 

#Cek angka negatif
if not bilangan_3.isnumeric():
    if bilangan_3[0] == '-' and len(bilangan_3) > 1:
        negatif += 1
    else:
        sys.exit("Inputan tidak valid")

bilangan_3 = int(bilangan_3)

#Cek angka genap dan ganjil
if bilangan_3 % 2 == 0 or bilangan_3 == 0:
    genap += 1
else:
    ganjil += 1

#Cek angka positif
if bilangan_3 > 0:
    positif += 1 

#Cek angka negatif
if not bilangan_4.isnumeric():
    if bilangan_4[0] == '-' and len(bilangan_4) > 1:
        negatif += 1
    else:
        sys.exit("Inputan tidak valid")

bilangan_4 = int(bilangan_4)

#Cek angka genap dan ganjil
if bilangan_4 % 2 == 0 or bilangan_4 == 0:
    genap += 1
else:
    ganjil += 1

#Cek angka positif
if bilangan_4 > 0:
    positif += 1 

#Cek angka negatif
if not bilangan_5.isnumeric():
    if bilangan_5[0] == '-' and len(bilangan_5) > 1:
        negatif += 1
    else:
        sys.exit("Inputan tidak valid")

bilangan_5 = int(bilangan_5)

#Cek angka genap dan ganjil
if bilangan_5 % 2 == 0 or bilangan_5 == 0:
    genap += 1
else:
    ganjil += 1

#Cek angka positif
if bilangan_5 > 0:
    positif += 1 

print (genap , "Angka genap")
print (ganjil, "Angka ganjil")
print (positif, "Angka positif")
print (negatif, "Angka negatif")