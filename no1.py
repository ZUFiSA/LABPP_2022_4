x = int(input(''))
def  factorial(x):
    if x == 0:
        return 1
    elif x < 0 :
        return ('Tidak terdefinisi')
    else:
        return (x * factorial(x-1))
print(factorial(x))