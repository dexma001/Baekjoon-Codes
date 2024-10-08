n = int(input())
answer = 0
for _ in range(n):
    if int(input()) % 2 != 0:
        answer += 1
print(answer)
