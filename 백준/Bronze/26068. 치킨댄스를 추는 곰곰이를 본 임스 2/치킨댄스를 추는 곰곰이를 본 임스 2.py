answer = 0
n = int(input())
for _ in range(n):
    temp = list(map(str, input().split('-')))
    if int(temp[-1]) <= 90:
        answer += 1
print(answer)
