# 2631

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]

for i in range(n):
    m = int(input())
    arr.append(m)

lis = [0] * (n+1)
lis[n] = 1

for i in range(n-1, 0, -1):
    lis[i] = 1
    for j in range(i+1, n+1):
        if arr[j] > arr[i]:
            lis[i] = max(lis[i], lis[j] + 1)

print(n - max(lis))
