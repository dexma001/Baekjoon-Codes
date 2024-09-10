# 21736

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
stack = deque()

for i in range(n):
    temp = list(map(str, input().rstrip()))
    if 'I' in temp:
        stack.append([i, temp.index('I')])
    arr.append(temp)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited = list(list(0 for _ in range(m)) for _ in range(n))
visited[stack[0][0]][stack[0][1]] = 1

answer = 0

while stack:
    a, b = stack.popleft()
    for i in range(4):
        y = a + dy[i]
        x = b + dx[i]
        if 0 <= y < n and 0 <= x < m:
            if arr[y][x] == 'X':
                continue
            elif arr[y][x] == 'O' and not visited[y][x]:
                visited[y][x] = 1
                stack.append([y, x])
            elif arr[y][x] == 'P' and not visited[y][x]:
                visited[y][x] = 1
                stack.append([y, x])
                answer += 1

if answer:
    print(answer)
else:
    print('TT')
