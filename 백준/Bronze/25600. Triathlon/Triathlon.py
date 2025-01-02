answer = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    temp = a*(b+c)
    if a == (b+c):
        temp *= 2

    answer = max(answer, temp)
print(answer)
