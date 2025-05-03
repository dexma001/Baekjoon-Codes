for _ in range(int(input())):
    temp = int(input())
    arr = list()
    for _ in range(temp//5):
        arr.append('++++')
    arr.append('|'*(temp%5))
    print(' '.join(arr))