# 16933

from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().strip())))

visited = list(list(list(0 for _ in range(m))
               for _ in range(n))for _ in range(k+1))
visited[0][0][0] = 1

queue = deque([])
queue.append([0, 0, 0, 1])  # n,m,k, dist

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while queue:
    p, q, r, dist = queue.popleft()
    if p == n-1 and q == m-1:
        print(dist)
        quit()

    day = dist % 2
    for i in range(4):
        y = p + dy[i]
        x = q + dx[i]

        if 0 <= y < n and 0 <= x < m:
            if arr[y][x] == 0 and not visited[r][y][x]:
                visited[r][y][x] = dist
                queue.append([y, x, r, dist+1])

            elif r < k and arr[y][x] == 1 and not visited[r+1][y][x]:
                if day:
                    visited[r+1][y][x] = dist
                    queue.append([y, x, r+1, dist+1])
                else:
                    queue.append([p, q, r, dist+1])

else:
    print(-1)
