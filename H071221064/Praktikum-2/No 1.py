#Konversi nilai dalam bentuk angka ke huruf
x = int(input('Nilai = '))

if x >= 90 and x <= 100:
    print("Nilai %s = 'A'"%(x))
elif x >= 80 and x < 90:
    print("Nilai %s = 'B'"%(x))
elif x >= 70 and x < 80:
    print("Nilai %s = 'C'"%(x))
elif x >= 60 and x < 70:
    print("Nilai %s = 'D'"%(x))
elif x >= 40 and x < 60:
    print("Nilai %s = 'E'"%(x))
elif x >= 0 and x < 40 :
    print("Nilai %s = 'F'"%(x))
else:
    print(x,'inputan salah, Masukkan nilai 0-100')