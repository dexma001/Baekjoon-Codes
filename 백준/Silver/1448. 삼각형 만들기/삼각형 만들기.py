# 1448

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

arr.sort()

answer = -1
for i in range(n-1, 1, -1):
    if arr[i] >= arr[i-1]+arr[i-2]:
        arr.pop(-1)
    else:
        answer = arr[i] + arr[i-1] + arr[i-2]
        break

print(answer)
