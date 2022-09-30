#Program dengan X sebagai banyak kolom dan secara horizontal

x = int(input("X : "))
y = int(input("Y : "))

if x < y:
    for i in range(1, y+1):
        print(i, end="\n" if i % x == 0 else " ")

else:
    print("Error")