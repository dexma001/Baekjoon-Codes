# 1261

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().strip())))

answer = 10001

stack = deque([])
stack.append([0, 0, 0])
visited = list(list(0 for _ in range(m)) for _ in range(n))
how_many_broken = list(list(10001 for _ in range(m)) for _ in range(n))
visited[0][0] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while stack:
    p, q, r = stack.popleft()
    if p == n-1 and q == m-1:
        answer = min(answer, r)
    for i in range(4):
        y = p + dy[i]
        x = q + dx[i]
        if 0 <= y < n and 0 <= x < m:
            if arr[y][x] == 1:
                if not visited[y][x]:
                    visited[y][x] = 1
                    how_many_broken[y][x] = r+1
                    stack.append([y, x, r+1])
                else:
                    if r+1 < how_many_broken[y][x]:
                        how_many_broken[y][x] = r+1
                        stack.append([y, x, r+1])
            else:
                if not visited[y][x]:
                    visited[y][x] = 1
                    how_many_broken[y][x] = r
                    stack.append([y, x, r])
                else:
                    if r < how_many_broken[y][x]:
                        how_many_broken[y][x] = r
                        stack.append([y, x, r])

print(answer)
