for _ in range(int(input())):
    value, name  = 0, ''
    for _ in range(int(input())):
        a, b = map(str, input().split())
        if int(a) > value:
            value = int(a)
            name = b
    print(name)