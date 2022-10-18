x = int(input('Hari :'))
def hitung_hari(x):
    tahun = x // 365
    sisa = x % 365
    bulan = sisa // 30
    hari = sisa % 30
    print('%d tahun' % (tahun))
    print('%d bulan' % (bulan))
    print('%d hari' % (hari))
hitung_hari(x)

