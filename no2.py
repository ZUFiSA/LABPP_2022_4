x = int(input(''))
y = int(input(''))
def FPB(x,y):
    if (y==0):
        return x
    else:
        return FPB(y,x%y)

if x == 0 or y == 0:
    print('- Infinity')
elif x < 0:
    print('FPB dari %d dan %d = %d' % (x,y,-FPB(x,y)))
elif y < 0:
    print('FPB dari %d dan %d = %d' % (x,y,FPB(x,y)))
else:
    print('FPB dari %d dan %d = %d' % (x,y,FPB(x,y)))