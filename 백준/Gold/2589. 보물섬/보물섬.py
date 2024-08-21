# 2589

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(list(map(str, input().rstrip())))

answer_visited = list(list(False for _ in range(m)) for _ in range(n))

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'W':
            continue
        else:
            stack = deque([])
            stack.append([i, j, 0])
            visited = list(list(False for _ in range(m)) for _ in range(n))
            visited[i][j] = True

            while stack:
                for _ in range(len(stack)):
                    temp = stack.popleft()
                    a = temp[0]
                    b = temp[1]
                    c = temp[2]
                    for k in range(4):
                        y = a + dy[k]
                        x = b + dx[k]
                        if 0 <= y < n and 0 <= x < m and arr[y][x] == 'L' and not visited[y][x]:
                            visited[y][x] = True
                            stack.append([y, x, c+1])
                    else:
                        answer = max(answer, c)

print(answer)
