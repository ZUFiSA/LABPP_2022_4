x = int(input(" Masukkan Nilai: "))
def factorial(x):

    if x < 0:
        return("Tak terdefinisi sob")
    elif x == 0:
        return 1
    else:
        return (x * factorial(x-1))
print(factorial(x))