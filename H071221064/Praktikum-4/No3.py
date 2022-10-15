def myDay():
    z = int(input())
    tahun = z // 365
    bulan = z % 365 // 30
    hari = z % 365 % 30
    print(tahun,'tahun')
    print(bulan,'bulan')
    print(hari,'hari')
myDay()
