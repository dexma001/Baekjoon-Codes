a, b = map(int, input().split())
x, y = map(int, input().split())

if a == 0:
    if y == 0:
        print(1)
    elif x == 0:
        if y < b:
            print(3)
        else:
            print(1)
    else:
        print(1)

elif b == 0:
    if x == 0:
        print(1)
    elif b == 0 and y == 0:
        if x < a:
            print(3)
        else:
            print(1)
    else:
        print(1)
else:
    print(2)
