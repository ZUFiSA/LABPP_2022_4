x = int(input("Horizontal x:"))
y = int(input("Range y:"))
if x<y:
    for i in range (1, y + 1):
        print (i, end='\n' if i % 2 == 0 else ' ')
else:
    print('x harus lebih kecil dari pada y')