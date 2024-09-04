# 3055

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list(map(str, input().rstrip())) for _ in range(n))

hedgedog = deque([])
water = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            hedgedog.append([i, j])
        elif arr[i][j] == '*':
            water.append([i, j])

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 0

while True:
    for _ in range(len(hedgedog)):
        c, d = hedgedog.popleft()
        if arr[c][d] != 'S':
            continue

        for j in range(4):
            y = c + dy[j]
            x = d + dx[j]
            if 0 <= y < n and 0 <= x < m:
                if arr[y][x] == 'D':
                    answer += 1
                    print(answer)
                    quit()

                if arr[y][x] == '.':
                    arr[y][x] = 'S'
                    hedgedog.append([y, x])

    for _ in range(len(water)):
        a, b = water.popleft()
        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if arr[y][x] == '.' or arr[y][x] == 'S':
                    arr[y][x] = '*'
                    water.append([y, x])

    if not hedgedog:
        print('KAKTUS')
        break

    answer += 1
