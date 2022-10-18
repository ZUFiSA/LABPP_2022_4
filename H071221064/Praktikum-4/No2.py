def getFPB(a,b):
    if (b==0):
        return a
    else:
        return getFPB(b,a%b)

a = int(input())
b = int(input())
if a == 0 or b == 0:
    print('-infinity')
elif a < 0:
    print('FPB dari %s dan %s ='%(a,b),-getFPB(a,b))
elif b < 0:
    print('FPB dari %s dan %s ='%(a,b),getFPB(a,b))
else:
    print('FPB dari %s dan %s ='%(a,b),getFPB(a,b))






