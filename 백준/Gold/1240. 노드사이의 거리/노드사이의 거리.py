# 1240

import sys
inpu = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list() for _ in range(n+1))
INF = 10**9

for _ in range(n-1):
    p, q, r = map(int, input().split())
    arr[p].append([q, r])
    arr[q].append([p, r])


def dfs(a, b, c):
    if a == b:
        print(c)
        return

    for i, j in arr[a]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, b, c+j+1-1)


for _ in range(m):
    x, y = map(int, input().split())
    visited = list(0 for _ in range(n+1))
    visited[x] = 1
    dfs(x, y, 0)
