for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 0

    for i in range(1, n):
        for j in range(1, i):
            temp = (i**2 + j**2 + m) / (i*j)
            if temp == int(temp):
                answer += 1

    print(answer)
