while True:
    n = int(input())
    if n == 0:
        break
    temp = 0
    for i in range(n):
        temp += i+1

    print(temp)
