#2206

import sys
input = sys.stdin.readline
from collections import deque
import time

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().strip())))
    
visited = list(list(list(0 for _ in range(m)) for _ in range(n)) for _ in range(2))
value = list(list(list(10e9 for _ in range(m)) for _ in range(n)) for _ in range(2))
stack = deque([])
stack.append([0, 0, 0])
visited[0][0][0] = 1
value[0][0][0] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while stack:
    for _ in range(len(stack)):
        i, j, k = stack.popleft()
        for l in range(4):
            y = i + dy[l]
            x = j + dx[l]
            if 0<=y<n and 0<=x<m and not visited[k][y][x]:
                if arr[y][x] == 1: 
                    if k == 0:
                        value[1][y][x] = min(value[1][y][x], value[0][i][j] + 1)
                        visited[1][y][x] = 1
                        stack.append([y, x, 1])
                    else:
                        continue
                else:
                    value[k][y][x] = min(value[k][y][x], value[k][i][j] + 1)
                    visited[k][y][x] = 1
                    stack.append([y, x, k])

print(-1) if min(value[0][-1][-1], value[1][-1][-1]) == 10e9 else print(min(value[0][-1][-1], value[1][-1][-1]))