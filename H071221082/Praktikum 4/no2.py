#Program menghitung Faktor Persekutuan Terbesar (FPB) dari dua inputan

a = int(input("Masukkan bilangan : "))
b = int(input("Masukkan bilangan : "))

def mencari_fpb(a,b):
    if a > b:
        bilangan_terbesar = a
    
    else:
        bilangan_terbesar = b
    
    for i in range (1, bilangan_terbesar+1):
        if a % i == 0 and b % i == 0:
            fpb = i

    return fpb

if a == 0 or b == 0:
    print ("- Infinity")

elif a < 0 or b < 0:
    print(f"-{mencari_fpb(a,b)}")

else:
    print(f"FPB ({a},{b}) = {mencari_fpb(a,b)}")