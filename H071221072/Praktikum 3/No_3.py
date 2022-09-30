a = int(input('a: '))
b = int(input('b: '))
kembalian = b - a
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if a < b:
    for i in uang:
        c = kembalian // i
        print('%d uang Rp. %d '% (c, i))
        kembalian = c * i
elif a == b:
    print('0')
else:
    print('Inputan b harus lebih besar dari pada a')