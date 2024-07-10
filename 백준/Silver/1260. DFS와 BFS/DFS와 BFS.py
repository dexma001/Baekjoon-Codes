# 1260

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs_visit = list()
bfs_visit = list()


def dfs(graph, k):
    dfs_visit.append(k)
    for i in graph[k]:
        if i not in dfs_visit:
            dfs(graph, i)


dfs(graph, v)

bfs_stack = deque([])
bfs_stack.append(v)
cnt = 1
while bfs_stack:
    for i in range(len(bfs_stack)):
        temp = bfs_stack.popleft()
        bfs_visit.append(temp)
        cnt += 1
        for j in graph[temp]:
            if j not in bfs_visit and j not in bfs_stack:
                bfs_stack.append(j)

print(*dfs_visit)
print(*bfs_visit)
