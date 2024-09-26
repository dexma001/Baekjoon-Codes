# 13023

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list([] for _ in range(n))

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = 0


def dfs(node, deep):
    global answer

    if deep == 5:
        answer = 1
        return

    for j in arr[node]:
        if not visited[j]:
            visited[j] = True
            dfs(j, deep+1)
            visited[j] = False

    return

    
for i in range(n):
    if not answer:
        visited = list(False for _ in range(n))
        visited[i] = True
        dfs(i, 1)

print(answer)
