# 3117

import math
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
first = list(map(int, input().split()))
algorithm = [0] + list(map(int, input().split()))

if m == 1:
    print(*first)
else:
    m -= 1
    sparse_table = list(list(0 for _ in range(k+1)) for _ in range(30))
    sparse_table[0] = algorithm

    for i in range(1, 30):
        for j in range(1, k+1):
            sparse_table[i][j] = sparse_table[i-1][sparse_table[i-1][j]]

    while m > 1:
        temp = math.floor(math.log(m, 2))
        for i in range(n):
            first[i] = sparse_table[temp][first[i]]
        m -= 2**temp

    if m != 0:
        for j in range(n):
            first[j] = sparse_table[0][first[j]]

    print(*first)
