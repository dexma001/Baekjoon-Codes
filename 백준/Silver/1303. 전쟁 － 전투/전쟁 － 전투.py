# 1303

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(m):
    arr.append(list(map(str, input().strip())))

visited = list(list(0 for _ in range(n)) for _ in range(m))

friendly = 0
enemy = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(m):
    for j in range(n):
        if visited[i][j] == 1:
            continue

        judge = arr[i][j]
        temp_answer = 1
        bfs = deque([])
        bfs.append([i, j])
        visited[i][j] = 1

        while bfs:
            p, q = bfs.popleft()
            for k in range(4):
                y = p + dy[k]
                x = q + dx[k]
                if 0 <= y < m and 0 <= x < n and arr[y][x] == judge:
                    if not visited[y][x]:
                        visited[y][x] = 1
                        temp_answer += 1
                        bfs.append([y, x])
        if judge == 'W':
            friendly += temp_answer ** 2
        else:
            enemy += temp_answer ** 2

print(friendly, enemy)
