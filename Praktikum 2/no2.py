
golongan = input('golongan = ').upper()
daya = float(input('daya = '))
Pemakaian = float(input('Pemakaian = '))

if golongan == 'R1':
    if daya == 900:
        print(f'jumlah tagihan anda: {Pemakaian * 1352:_}'.replace('.',',').replace('_','.'))
if golongan == 'R1':
    if daya == 1300 or daya == 2200:
        print(f'jumlah tagihan anda: {Pemakaian * 1444.70:_}'.replace('.',',').replace('_','.'))
    elif daya != 900 and daya != 1300 and daya != 2200:
        print('Golongan R1 hanya memiliki daya 900, 1300, dan 2200')
    # elif daya < 1300 and daya > 1300 and daya <= 2200 and daya > 2200:
    #     ('Golongan R1 hanya memiliki daya 900, 1300, dan 2200')
elif golongan == 'R2':
    if daya >= 3500 and daya <= 5500:
        print(f'jumlah tagihan anda: {Pemakaian * 1699.53:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
elif golongan == 'R3':
    if daya >= 6600:
        print(f'jumlah tagihan anda: {Pemakaian * 1699.53:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
elif golongan == 'B2':
    if daya >= 6600 and daya <=200000:
        print(f'jumlah tagihan anda: {Pemakaian * 1444.70:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
elif golongan == 'B3':
    if daya > 200000:
        print(f'jumlah tagihan anda: {Pemakaian * 1114.74:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
elif golongan == 'I3':
    if daya >= 200000:
        print(f'jumlah tagihan anda: {Pemakaian * 1314.12:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
elif golongan == 'P1':
    if daya >=6600 and daya <= 200000:
        print(f'jumlah tagihan anda: {Pemakaian * 1523.28:_}'.replace('.',',').replace('_','.'))
    else:
        print('data tidak valid')
else:
    print('golongan tidak valid')
