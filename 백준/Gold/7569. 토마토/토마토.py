import sys
from collections import deque

p, q, r = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split()))
          for _ in range(q)] for _ in range(r)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(day):
    while queue:
        day += 1
        for _ in range(len(queue)):
            a, b, c = queue.popleft()
            for i in range(6):
                x = a + dx[i]
                y = b + dy[i]
                z = c + dz[i]

                if -1 < x < r and -1 < y < q and -1 < z < p and graph[x][y][z] == 0:
                    graph[x][y][z] = 1
                    queue.append([x, y, z])

    for e in range(r):
        for f in range(q):
            for g in range(p):
                if graph[e][f][g] == 0:
                    return -1

    return day - 1


queue = deque([])
for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(len(graph[i][j])):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

print(bfs(0))
