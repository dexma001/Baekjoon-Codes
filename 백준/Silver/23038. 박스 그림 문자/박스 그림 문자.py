# 23038

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(3*n):
    arr.append(list(map(str, input().strip())))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(1, 3*n-1, 3):
    for j in range(1, 3*m-1, 3):
        if arr[i][j] != '#':
            continue

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]

            if arr[y][x] == '#':
                if k == 0:
                    arr[y+2][x] = '#'
                    arr[y+1][x] = '#'
                elif k == 1:
                    arr[y][x+2] = '#'
                    arr[y][x+1] = '#'
                elif k == 2:
                    arr[y-2][x] = '#'
                    arr[y-1][x] = '#'
                else:
                    arr[y][x-2] = '#'
                    arr[y][x-1] = '#'

for i in arr:
    print(''.join(i))
