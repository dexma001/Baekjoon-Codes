# 11404

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(list(2e32 for _ in range(n)) for _ in range(n))

for i in range(n):
    li[i][i] = 0

for i in range(m):
    a, b, i = map(int, input().split())
    li[a-1][b-1] = min(li[a-1][b-1], i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            li[i][j] = min(li[i][j], li[i][k]+li[k][j])

for v in range(n):
    for w in range(n):
        if li[v][w] == 2e32:
            li[v][w] = 0

for u in range(n):
    ans = li[u]
    print(*ans)
