# 2665

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().rstrip())) for _ in range(n))

stack = deque([])
stack.append([0, 0, 0])

visited = list(list(-1 for _ in range(n)) for _ in range(n))
visited[0][0] = 0

answer = 200

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while stack:
    for _ in range(len(stack)):
        a, b, c = stack.popleft()
        if a == n-1 and b == n-1:
            answer = min(answer, c)
            continue

        for i in range(4):
            y = a + dy[i]
            x = b + dx[i]
            if 0 <= y < n and 0 <= x < n:
                if arr[y][x] == 1:
                    if visited[y][x] != -1 and c < visited[y][x]:
                        visited[y][x] = c
                        stack.append([y, x, c])
                    elif visited[y][x] == -1:
                        visited[y][x] = c
                        stack.append([y, x, c])

                else:
                    if visited[y][x] != -1 and c+1 < visited[y][x]:
                        visited[y][x] = c+1
                        stack.append([y, x, c+1])
                    elif visited[y][x] == -1:
                        visited[y][x] = c+1
                        stack.append([y, x, c+1])

print(answer)
