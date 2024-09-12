# 11403

import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    visited = list(0 for _ in range(n))
    stack = list()
    for j in range(n):
        if arr[i][j] == 1:
            stack.append(j)
    while stack:
        p = stack.pop(0)
        for k in range(n):
            if arr[p][k] == 1 and not visited[k]:
                visited[k] = 1
                arr[i][k] = 1
                stack.append(k)

for q in arr:
    print(*q)
