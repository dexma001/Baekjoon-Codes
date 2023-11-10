# topological logic

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)  # 각 숫자의 진입차수
graph = [[] for _ in range(n+1)]  # a가 진입하는 숫자들
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    for i in result:
        print(i, end=' ')


topology_sort()
