# 2206

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list(map(int, input().strip()))for _ in range(n))
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([])
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])

                elif arr[nx][ny] == 1 and z == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append([nx, ny, z+1])
    return -1


print(bfs())
