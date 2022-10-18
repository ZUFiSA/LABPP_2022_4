#Program pergerakan robot

def robot():
    x = 0
    y = 0
    while True:
        s = input().upper()
        if s == "START":
            x = 0
            y = 0
            print(x,y)
            continue
        elif s == "R":
            x += 1
            print(x,y)
        elif s == "L":
            x -= 1
            print(x,y)
        elif s == "U":
            y += 1
            print(x,y)
        elif s == "D":
            y -= 1
            print(x,y)
        elif s == "END":
            exit()

robot()

