# 10868

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

height = list(0 for _ in range(n+1))
for i in range(2, n+1):
    height[i] = height[i >> 1]+1

sparse_table = list(list(0 for _ in range(n+1))
                    for _ in range(height[-1]+1))
sparse_table[0] = arr

step = 1
for i in range(1, height[-1]+1):
    for j in range(1, n+1):
        if j + step < n+1:
            sparse_table[i][j] = min(
                sparse_table[i-1][j], sparse_table[i-1][j+step])
    step <<= 1

for _ in range(m):
    a, b = map(int, input().split())
    temp = b-a+1
    r = height[temp]
    print(min(sparse_table[r][a], sparse_table[r][b+1 - 2**(r)]))
