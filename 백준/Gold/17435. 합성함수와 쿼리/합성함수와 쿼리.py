# 17435

import math
import sys
input = sys.stdin.readline

m = int(input())
arr = [0] + list(map(int, input().split()))

sparse_table = [arr] + list(list(0 for _ in range(m+1))
                            for _ in range(19))

for i in range(1, 20):
    for j in range(1, m+1):
        sparse_table[i][j] = sparse_table[i-1][sparse_table[i-1][j]]

for i in range(int(input())):
    n, x = map(int, input().split())

    while n > 1:
        temp = int(math.log(n, 2))
        x = sparse_table[temp][x]
        n -= 2**temp

    if n == 0:
        print(x)
    else:
        print(arr[x])
