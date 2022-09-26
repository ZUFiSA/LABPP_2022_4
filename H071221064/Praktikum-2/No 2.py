a = input('golongan = ').upper()
x = float(input('daya = '))
pemakaian = float(input('pemakaian = '))

if a =='R1':
    if x ==900:
        print(f'jumlah tagihan anda: {1352*pemakaian:_}'.replace('.',',').replace('_','.'))
    elif x ==1300:
        print(f'jumlah tagihan anda: {1444.70*pemakaian:_}'.replace('.',',').replace('_','.'))
    elif x ==2200:
        print(f'jumlah tagihan anda: {1444.70*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print('Golongan R1 hanya memiliki daya 900, 1300 dan 2200')

elif a =='R2':
    if x >=3500 and x <=5500:
        print(f'jumlah tagihan anda: {1699.53*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

elif a =='R3':
    if x >=6600:
        print(f'jumlah tagihan anda: {1699.53*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

elif a =='B2':
    if x >=6600 and x <=200000:
        print(f'jumlah tagihan anda: {1444.70*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

elif a =='B3':
    if x >200000:
        print(f'jumlah tagihan anda: {1114.74*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

elif a =='I3':
    if x >=200000:
        print(f'jumlah tagihan anda: {1314.12*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

elif a =='P1':
    if x >= 6600 and x <=200000:
        print(f'jumlah tagihan anda: {1523.28*pemakaian:_}'.replace('.',',').replace('_','.'))
    else:
        print("Inputan Tidak Valid")

else:
    print("Inputan Tidak Valid")
