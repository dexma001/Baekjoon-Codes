# 6593

import sys
from collections import deque
input = sys.stdin.readline

while True:
    l, r, c = map(int, input().split())

    if [l, r, c] == [0, 0, 0]:
        break

    arr = list()

    pos = deque([])

    for i in range(l):
        temp = list()
        for j in range(r):
            ttemp = list(map(str, input().strip()))
            if 'S' in ttemp:
                pos.append([i, j, ttemp.index('S')])
            elif 'E' in ttemp:
                end = [i, j, ttemp.index('E')]
            temp.append(ttemp)
        arr.append(temp)
        p = input()

    visited = list(list(list(0 for _ in range(c))
                   for _ in range(r)) for _ in range(l))

    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]

    visited[0][0][0] = 1

    answer = 100000
    cnt = 0
    while pos:
        for _ in range(len(pos)):
            i, j, k = pos.popleft()
            if [i, j, k] == end:
                answer = min(answer, cnt)
                break

            for p in range(6):
                z = i + dz[p]
                y = j + dy[p]
                x = k + dx[p]

                if 0 <= z < l and 0 <= y < r and 0 <= x < c:
                    if arr[z][y][x] != '#' and not visited[z][y][x]:
                        visited[z][y][x] = 1
                        pos.append([z, y, x])

        cnt += 1

    print(f"Escaped in {answer} minute(s).") if answer != 100000 else print(
        'Trapped!')
