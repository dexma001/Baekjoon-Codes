import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
p, q, r = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

li[p][q] = 2
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        nx = p + dx[(r+3) % 4]
        ny = q + dy[(r+3) % 4]
        r = (r+3) % 4
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 0:
            li[nx][ny] = 2
            cnt += 1
            p = nx
            q = ny
            flag = 1
            break
    if flag == 0:
        if li[p-dx[r]][q-dy[r]] == 1:
            print(cnt)
            break
        else:
            p, q = p-dx[r], q-dy[r]
