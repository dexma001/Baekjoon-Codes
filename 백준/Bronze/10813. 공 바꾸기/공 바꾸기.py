# 10813

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(i for i in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

print(*arr[1:])
