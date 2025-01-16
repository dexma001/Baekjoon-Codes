n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = list(0 for _ in range(n))
for i in range(n):
    for j in range(n):
        if i != j:
            answer[i] = answer[i] | arr[i][j]

print(*answer)
