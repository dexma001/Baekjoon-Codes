for _ in range(int(input())):
    n = str(bin(int(input())))
    arr = list()
    for i in range(len(n)):
        if n[i] == '1':
            arr.append(len(n) - i-1)
    arr.sort()
    print(*arr)
