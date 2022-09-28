nilai = int(input('masukkan nilai dalam angka 1 - 100: '))

if nilai >= 90 and nilai <= 100:
    print("nilai  %s = 'A'"%(nilai))
elif nilai >= 80 and nilai <= 89:
    print("nilai %s = 'B'"%(nilai))
elif nilai >= 70 and nilai <= 79:
    print("nilai %s = 'C'"%(nilai))
elif nilai >= 60 and nilai <= 69:
    print("nilai %s = 'D'"%(nilai))
elif nilai >= 40 and nilai <= 59:
     print("nilai %s = 'E'"%(nilai))
elif nilai < 40 and nilai > 0:
    print("nilai %s = 'F'"%(nilai))

else:
    print('nilai salah, masukkan nilai 1 - 100')

