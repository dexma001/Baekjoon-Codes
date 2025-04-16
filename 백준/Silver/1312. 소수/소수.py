a, b, n = map(int, input().split())

answer = 0

for _ in range(n+1):
    answer = a//b
    a = (a % b) * 10

print(answer)
