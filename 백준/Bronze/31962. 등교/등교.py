n, m = map(int, input().split())
answer = -1

for _ in range(n):
    a, b = map(int, input().split())
    if a+b <= m:
        answer = max(answer, a)

print(answer)
