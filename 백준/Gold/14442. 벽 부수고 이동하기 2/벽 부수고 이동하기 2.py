# 14442

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(list(map(int, input().rstrip())) for _ in range(n))
answer = list(list([0]*(k+1) for _ in range(m))
              for _ in range(n))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

stack = deque([])
stack.append([0, 0, 0])
answer[0][0][0] = 1
visited = list(list([0]*(k+1) for _ in range(m))for _ in range(n))


while stack:
    x, y, z = stack.popleft()

    if x == n-1 and y == m-1:
        print(answer[x][y][z])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z]:
            if arr[nx][ny] == 0 and answer[nx][ny][z] == 0:
                answer[nx][ny][z] = answer[x][y][z] + 1
                stack.append([nx, ny, z])
                visited[nx][ny][z] = 1

            elif arr[nx][ny] == 1 and z < k:
                answer[nx][ny][z+1] = answer[x][y][z] + 1
                stack.append([nx, ny, z+1])
                visited[nx][ny][z] = 1
else:
    print(-1)
