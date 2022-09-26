Nilai = int(input('Nilai = '))

if Nilai >= 90 and Nilai <= 100:
    print("> nilai %s ='A'"%(Nilai))
elif Nilai >= 80 and Nilai <=89:
    print("> nilai %s ='B'"%(Nilai))
elif  Nilai >= 70 and Nilai <=79:
    print("> nilai %s ='C'"(Nilai))
elif  Nilai >= 60 and Nilai <=69:
   print("> nilai %s ='D'"%(Nilai))
elif  Nilai >= 40 and Nilai <=59:
   print("> nilai %s ='E'"%(Nilai))
elif  Nilai < 40 and Nilai > 0:
    print("> nilai %s ='F'"%(Nilai))
elif Nilai == 0:
    print('Yang bener dek')
else:
    print("Inputan salah, Masukkan nilai 0 - 100")

