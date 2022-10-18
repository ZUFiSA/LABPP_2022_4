#Program menghitung faktorial

n = int(input('Masukkan nilai n: '))

def hitung_faktorial (n):
    if n > 0:
        return n * hitung_faktorial(n - 1)
    return 1

faktorial = hitung_faktorial(n)
if n >= 0:
    print(f'{n}! = {faktorial}')

elif n < 0:
    print("Tidak Terdefinisi")