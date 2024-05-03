# 2638

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph[0][0] = 2


def outside(a, b):
    for i in range(4):
        x1 = a + dx[i]
        y1 = b + dy[i]

        if 0 <= x1 < n and 0 <= y1 < m and graph[x1][y1] == 0:
            graph[x1][y1] = 2
            outside(x1, y1)


outside(0, 0)

cheese_arr = list()
stack = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese_arr.append((i, j))
            det_to_delete = 0
            for k in range(4):
                x1 = i + dx[k]
                y1 = j + dy[k]
                if 0 <= x1 < n and 0 <= y1 < m and graph[x1][y1] == 2:
                    det_to_delete += 1
            if det_to_delete >= 2:
                stack.append((i, j))


answer = 0
while stack:
    for _ in range(len(stack)):
        a, b = stack.popleft()

        cheese_arr.remove((a, b))
        graph[a][b] = 2
        for i in range(4):
            a1 = a + dx[i]
            b1 = b + dy[i]
            if graph[a1][b1] == 0:
                graph[a1][b1] = 2
                outside(a1, b1)

    for p in range(len(cheese_arr)):
        c, d = cheese_arr[p]
        det_to_delete = 0
        for q in range(4):
            c1 = c + dx[q]
            d1 = d + dy[q]
            if 0 <= c1 < n and 0 <= d1 < m and graph[c1][d1] == 2:
                det_to_delete += 1
        if det_to_delete >= 2:
            stack.append((c, d))
    answer += 1

print(answer)
