# 2178

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (m+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().rstrip())))

visited = list(list(0 for _ in range(m+1)) for _ in range(n+1))
visited[1][1] = 1
stack = deque([[1, 1]])
answer = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while stack:
    for _ in range(len(stack)):
        a, b = stack.popleft()
        if a == n and b == m:
            print(answer+1)
            quit()
        else:
            for j in range(4):
                da = a + dx[j]
                db = b + dy[j]
                if 1 <= da <= n and 1 <= db <= m and arr[da][db] == 1 and visited[da][db] == 0:
                    stack.append([da, db])
                    visited[da][db] = 1
    answer += 1
