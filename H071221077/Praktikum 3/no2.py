nilai = int(input('Masukkan angka : '))
angka1 = 0
angka2 = 1

for i in range(nilai):
    print(angka1, end=' ')
    angka_selanjutnya = angka1 + angka2
    angka1 = angka2
    angka2 = angka_selanjutnya
    
#angka=5
#angka1=0, terus angka2= 1
#perulangan pertama: i:0
#print(0)
#angka_selanjutnya: 0+1,
#angka1= angka2: 1
#angka2= angka_selanjutnya: 1
#perulangan kedua: i:1
#print(0 1)
#angka_selanjutnya : 1+1
#angka1= angka2: 1
#angka2= angka_selanjutnya : 2
#perulangan ketiga: i:2
#print(0 1 1)
#angka_selanjutnya : 1+2
#angka1 = angka2 : 2
#angka2= angka_selanjutnya : 3
#perulangan keempat : i:3
#print (0 1 1 2)
#angka_selanjutnya : 2+3
#angka1= angka2: 3
#angka2= angka_selanjutnya : 5
#perulangan kelima : i:4
#print (0 1 1 2 3)
#angka_selanjutnya : 3+5
#angka1= angka2: 5
#angka2= angka_selanjutnya : 8