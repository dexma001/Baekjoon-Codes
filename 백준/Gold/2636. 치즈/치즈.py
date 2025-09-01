# 2636

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
cnt = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while True:
    temp = deque([])
    temp.append([0, 0])
    cheese_to_melt = list()
    visited = list(list(0 for _ in range(m)) for _ in range(n))

    if not cnt:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    cnt += 1

    while temp:
        y, x = temp.popleft()

        for k in range(4):
            ddy = y + dy[k]
            ddx = x + dx[k]
            if 0 <= ddy < n and 0 <= ddx < m:
                if visited[ddy][ddx]:
                    continue
                visited[ddy][ddx] = 1
                if arr[ddy][ddx] == 1:
                    cheese_to_melt.append([ddy, ddx])
                else:
                    temp.append([ddy, ddx])

    for p, q in cheese_to_melt:
        arr[p][q] = 0

    answer += 1

    temp_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                temp_cnt += 1

    if temp_cnt == 0:
        break
    else:
        cnt = temp_cnt

print(answer)
print(cnt)
