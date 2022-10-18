x = int(input("Masukkan nilai: "))

def faktorial(x):
    if x == 1 or x == 0:
        return 1
    elif x < 0:
        return "tidak terdefinisi"
    else:
        return x * faktorial(x-1)
print("faktorial:", faktorial(x))