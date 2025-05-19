n = int(input())
answer = 0

for i in range(1, n+1):
    y = str(i)
    suu = sum(map(int, y))
    if i % suu == 0:
        answer += 1

print(answer)
