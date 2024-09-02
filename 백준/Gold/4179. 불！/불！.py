# 4179

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(input().rstrip()))

jee = deque([])
fire = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':
            jee.append([i, j])
        elif arr[i][j] == 'F':
            fire.append([i, j])

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 1

while True:
    will_fire = list()
    for _ in range(len(fire)):
        a, b = fire.popleft()
        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if [y, x] == 'J':
                    will_fire.append([y, x])
                elif arr[y][x] == '.':
                    arr[y][x] = 'F'
                    fire.append([y, x])

    for _ in range(len(jee)):
        c, d = jee.popleft()
        if arr[c][d] == 'F':
            continue

        if c == 0 or c == n-1 or d == 0 or d == m-1:
            print(1)
            quit()
        for j in range(4):
            p = c + dy[j]
            q = d + dx[j]
            if p < 0 or p >= n or q < 0 or q >= m:
                continue

            if p == 0 or p == n-1 or q == 0 or q == m-1:
                if arr[p][q] == '.':
                    print(answer + 1)
                    quit()

            else:
                if arr[p][q] == '.':
                    arr[p][q] = 'J'
                    jee.append([p, q])

    for v, w in will_fire:
        arr[v, w] = 'F'

    if not jee:
        print('IMPOSSIBLE')
        break

    answer += 1
