import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(day):
    while queue:
        day += 1
        for _ in range(len(queue)):
            a, b = queue.popleft()
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]

                if -1 < x < n and -1 < y < m and graph[x][y] == 0:
                    graph[x][y] = 1
                    queue.append([x, y])

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1

    return day - 1


queue = deque([])
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            queue.append([i, j])

print(bfs(0))
