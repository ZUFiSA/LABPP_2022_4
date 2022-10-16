def hitung_FPB(x,y):
    if (y==0):
        return x
    else:
        return hitung_FPB(y,x%y)

x = int(input(''))
y = int(input(''))
if x == 0 or y == 0:
    print('- infinity')
elif x < 0:
    print(f'FPB dari {x} dan {y} = {-hitung_FPB(x,y)}')
elif y < 0:
    print(f'FPB dari {x} dan {y} = {hitung_FPB(x,y)}')
else:
    print(f'FPB dari {x} dan {y} = {hitung_FPB(x,y)}')