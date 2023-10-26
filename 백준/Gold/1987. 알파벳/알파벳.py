import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0


def dfs(x, y, cnt):
    global ans

    ans = max(ans, cnt)
    visited.add(graph[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in visited:
            dfs(nx, ny, cnt+1)

    visited.remove(graph[x][y])


dfs(0, 0, 1)

print(ans)
