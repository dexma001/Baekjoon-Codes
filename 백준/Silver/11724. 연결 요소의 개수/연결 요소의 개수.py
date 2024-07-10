# 11724

import sys
sys.setrecursionlimit(2**31-1)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = list(False for _ in range(n+1))


def dfs(k):
    if visited[k]:
        return
    else:
        visited[k] = True
        for i in graph[k]:
            if not visited[i]:
                dfs(i)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
