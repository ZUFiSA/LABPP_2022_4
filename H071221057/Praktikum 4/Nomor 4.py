def program_robot():
    baris_horizontal = 0
    garis_vertikal = 0
    while True:
        a = input().lower()
        if a == 'start':
            baris_horizontal = 0
            garis_vertikal = 0
            print(baris_horizontal,garis_vertikal)
            continue
        elif a == 'end':
            exit()
        elif baris_horizontal == 0 and garis_vertikal == 0:
            print(baris_horizontal,garis_vertikal)
        for i in a:
            if i == 'r':
                baris_horizontal += 1
                print(baris_horizontal,garis_vertikal)
            elif i == 'l':
                baris_horizontal -= 1
                print(baris_horizontal,garis_vertikal)
            elif i == 'u':
                garis_vertikal += 1
                print(baris_horizontal,garis_vertikal)
            elif i == 'd':
                garis_vertikal -= 1
                print(baris_horizontal,garis_vertikal)
program_robot()

