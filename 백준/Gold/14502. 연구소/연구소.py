# 14502

from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = list(list(map(int, input().split())) for _ in range(n))
coords = [[x, y] for x in range(n) for y in range(m) if graph[x][y] == 0]
virus = deque([[x, y] for x in range(n) for y in range(m) if graph[x][y] == 2])
com = deque(list(combinations(coords, 3)))
ans = set()

for i in range(len(com)):
    graph1 = deepcopy(graph)
    virus1 = deepcopy(virus)
    a, b, c = com.popleft()
    for j in (a, b, c):
        graph1[j[0]][j[1]] = 1

    while virus1:
        x, y = virus1.popleft()

        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]

            if 0 <= nx < n and 0 <= ny < m and graph1[nx][ny] == 0:
                graph1[nx][ny] = 2
                virus1.append([nx, ny])
    li = [(x, y) for x in range(n) for y in range(m) if graph1[x][y] == 0]
    ans.add(len(li))

print(max(ans))
