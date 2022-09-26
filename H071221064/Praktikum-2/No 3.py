import sys
genap = 0
ganjil = 0
positif = 0
negatif = 0

a,b,c,d,e = input().split() 
#mengecek negatif
if not a.isnumeric(): 
    if a[0] == '-': 
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
a = int(a)
#mengecek ganjil genap
if a %2==0 or a == 0:
    genap+=1
else:
    ganjil+=1
#mengecek positif
if a>0:
    positif+=1

#mengecek negatif
if not b.isnumeric():
    if b[0] == '-':
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
b = int(b)
# mengecek ganjil genap
if b %2==0 or b == 0:
    genap+=1
else:
    ganjil+=1
# mengecek positif
if b>0:
    positif+=1

#mengecek negatif
if not c.isnumeric():
    if c[0] == '-':
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
c = int(c)
#mengecek ganjil genap
if c %2==0 or c == 0:
    genap+=1
else:
    ganjil+=1
#mengecek positif
if c>0:
    positif+=1

#mengecek negatif
if not d.isnumeric():
    if d[0] == '-':
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
d = int(d)
#mengecek ganjil genap
if d %2==0 or d == 0:
    genap+=1
else:
    ganjil+=1
#mengecek positif
if d>0:
    positif+=1

#mengecek negatif
if not e.isnumeric():
    if e[0] == '-':
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
e = int(e)
#mengecek ganjil genap
if e %2==0 or e == 0:
    genap+=1
else:
    ganjil+=1
#mengecek positif
if e>0:
    positif+=1

print (genap , "Angka genap")
print (ganjil, "Angka ganjil")
print (positif, "Angka positif")
print (negatif, "Angka negatif")

