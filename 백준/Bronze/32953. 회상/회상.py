from collections import defaultdict

n, m = map(int, input().split())
arr = defaultdict(int)

for _ in range(n):
    t = int(input())
    temp = list(map(int, input().split()))
    for i in temp:
        arr[i] += 1

answer = 0
for i, j in enumerate(arr):
    if arr[j] >= m:
        answer += 1
print(answer)
