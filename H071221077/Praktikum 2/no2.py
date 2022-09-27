golongan = (input('Golongan = ')).upper()
daya = int(input('Daya = '))
Pemakaian = int(input('Pemakaian(kWh) = '))

match golongan.upper():
    case "R1":
        if golongan == 'R1' and daya == 900:
            tarif = 1352
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        elif daya == 1300 or daya == 2200:
            tarif = 1444.70
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print("Golongan R1 hanya memiliki daya 900, 1300 dan 2200")

    case "R2":
        if daya >= 3500 and daya <= 5500:
            tarif = 1699.53
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('data tidak valid')

    case "R3":
        if daya >= 6600:
            tarif = 1699.53
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))

    case "B2":
        if daya >= 6000 and daya <= 200000:
            tarif = 1444.70
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('data tidak valid')

    case "B3":
        if daya > 200000:
            tarif = 1114.74
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('data tidak valid')

    case "I3":
        if daya >= 200000:
            tarif = 1314.12
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('data tidak valid')

    case "P1":
        if daya >= 6600 and daya <= 200000:
            tarif = 1523.28
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('data tidak valid')

    case _:
        print('data tidak valid')