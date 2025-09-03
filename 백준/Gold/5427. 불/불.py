# 5427

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = list()

    starting = deque([])
    fire_list = deque([])
    for i in range(h):
        temp = list(map(str, input().strip()))
        for j in range(w):
            if temp[j] == '@':
                starting.append([i, j])
            elif temp[j] == '*':
                fire_list.append([i, j])
            else:
                continue
        arr.append(temp)

    answer = 0
    visited = list(list(0 for _ in range(w)) for _ in range(h))
    visited[starting[0][0]][starting[0][1]] = 1
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    breaker = 0
    while starting:
        if breaker:
            break

        for _ in range(len(starting)):
            if breaker:
                break
            y, x = starting.popleft()
            if arr[y][x] == '*':
                continue
            for i in range(4):
                ddy = y + dy[i]
                ddx = x + dx[i]
                if ddy < 0 or ddy >= h or ddx < 0 or ddx >= w:
                    answer += 1
                    breaker = 1
                    break

                else:
                    if visited[ddy][ddx] or arr[ddy][ddx] == '#' or arr[ddy][ddx] == '*':
                        continue
                    visited[ddy][ddx] = 1
                    arr[ddy][ddx] = '@'
                    starting.append([ddy, ddx])

        if breaker:
            break

        for _ in range(len(fire_list)):
            y, x = fire_list.popleft()

            for j in range(4):
                ddy = y + dy[j]
                ddx = x + dx[j]

                if 0 <= ddy < h and 0 <= ddx < w:
                    if arr[ddy][ddx] == '#' or arr[ddy][ddx] == '*':
                        continue
                    else:
                        arr[ddy][ddx] = '*'
                        fire_list.append([ddy, ddx])

        answer += 1

    print('IMPOSSIBLE') if not breaker else print(answer)
