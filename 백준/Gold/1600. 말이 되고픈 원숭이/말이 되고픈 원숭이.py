# 1600

from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = list(list(list(0 for _ in range(k+1))
               for _ in range(m)) for _ in range(n))
visited[0][0][0] = 1

answer = deque([])
answer.append([[0, 0], 0])


dy = [1, 0, -1, 0, 2, 1, -1, -2, -2, -1, 1, 2]
dx = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]

cnt = 0
while True:
    for _ in range(len(answer)):
        a, b = answer.popleft()
        if a[0] == n-1 and a[1] == m-1:
            print(cnt)
            quit()

        for i in range(4):
            y = a[0] + dy[i]
            x = a[1] + dx[i]
            if 0 <= y < n and 0 <= x < m and arr[y][x] == 0 and not visited[y][x][b]:
                visited[y][x][b] = 1
                answer.append([[y, x], b])

        if b < k:
            for j in range(4, 12):
                y = a[0] + dy[j]
                x = a[1] + dx[j]
                if 0 <= y < n and 0 <= x < m and arr[y][x] == 0 and not visited[y][x][b+1]:
                    visited[y][x][b+1] = 1
                    answer.append([[y, x], b+1])

    if not answer:
        print(-1)
        break

    cnt += 1
