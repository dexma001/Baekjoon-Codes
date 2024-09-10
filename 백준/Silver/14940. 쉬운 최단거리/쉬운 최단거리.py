# 14940

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list()
stack = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    if not stack and 2 in temp:
        stack.append([i, temp.index(2)])
    arr.append(temp)

answer = list(list(0 for _ in range(m)) for _ in range(n))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
ans = 1

while stack:
    for _ in range(len(stack)):
        p, q = stack.popleft()
        for i in range(4):
            y = p + dy[i]
            x = q + dx[i]
            if 0 <= y < n and 0 <= x < m and arr[y][x] == 1 and not answer[y][x]:
                answer[y][x] = ans
                stack.append([y, x])
    ans += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not answer[i][j]:
            answer[i][j] = -1

for i in answer:
    print(*i)
