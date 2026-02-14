n = int(input())

sec = [300, 60, 10]
answer = list()

if n % 10 == 0:
    for i in range(3):
            answer.append(n//sec[i])
            n -= n//sec[i] * sec[i]
    print(*answer)
else:
    print(-1)