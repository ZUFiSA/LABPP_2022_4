x = int(input("masukkan : "))
y = int(input("masukkan : "))

def hitung_fpb(x, y):
    if (y == 0):
        return x
    else:
        return hitung_fpb(y, x % y)

if x == 0 or y == 0:
    print('-infinity')
elif x < 0:
    print(f'FPB dari {x} dan {y} = {-hitung_fpb(x,y)}')
elif y < 0:
    print(f'FPB dari {x} dan {y} = {hitung_fpb(x,y)}')
else:
    print(f'FPB dari {x} dan {y} = {hitung_fpb(x,y)}')