# 2230

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr.sort()

i, j = 0, 0
answer = 2000000001

while True:
    if arr[j] - arr[i] >= m:
        answer = min(answer, arr[j] - arr[i])

    if i == n-1 and j == n-1:
        break

    if j == n-1:
        i += 1
    elif i == j or arr[j] - arr[i] < m:
        j += 1
    else:
        i += 1


print(answer)
