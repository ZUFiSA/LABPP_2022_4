#Mengkonversi nilai dalam bentuk angka ke huruf

nilai = int(input("Nilai = "))

if nilai >= 90 and nilai <= 100:
    print ("niai" , nilai , "= `A`")

elif nilai >= 80 and nilai <= 100:
    print ("niai" , nilai , "= `B`")

elif nilai >= 70 and nilai <= 100:
    print ("niai" , nilai , "= `C`")

elif nilai >= 60 and nilai <= 100:
    print ("niai" , nilai , "= `D`")

elif nilai >= 40 and nilai <= 100:
    print ("niai" , nilai , "= `E")

elif nilai < 40 and nilai >=0:
    print ("niai" , nilai , "= `F`")

else:
    print (nilai , "Inputan salah, Masukkan nilai 0-100")
