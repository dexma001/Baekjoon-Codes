# 11967

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = list(list(0 for _ in range(n+1)) for _ in range(n+1))
switch = defaultdict(list)

for _ in range(m):
    x, y, a, b = map(int, input().split())
    switch[x, y].append([a, b])

visited = list(list(0 for _ in range(n+1)) for _ in range(n+1))

maze[1][1] = 1
stack = deque([])
stack.append([1, 1])
visited[1][1] = 1
answer = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while stack:
    i, ii = stack.popleft()

    if maze[i][ii] == 0:
        continue

    if switch[i, ii]:
        for j, jj in switch[i, ii]:
            if not maze[j][jj]:
                maze[j][jj] = 1
                for l in range(4):
                    y1 = j + dy[l]
                    x1 = jj + dx[l]
                    if 1 <= y1 <= n and 1 <= x1 <= n and visited[y1][x1]:
                        stack.appendleft([y1, x1])
                answer += 1

    for k in range(4):
        y = i + dy[k]
        x = ii + dx[k]

        if 1 <= y <= n and 1 <= x <= n and not visited[y][x]:
            if maze[y][x] == 1:
                visited[y][x] = 1
                stack.appendleft([y, x])
            else:
                stack.append([y, x])

print(answer)
