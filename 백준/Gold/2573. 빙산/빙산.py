# 2573

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 0

while True:
    temp = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                for k in range(4):
                    if arr[i+dy[k]][j+dx[k]] == 0:
                        temp[i, j] += 1

    answer += 1

    for i, j in temp:
        if temp[(i, j)] > arr[i][j]:
            arr[i][j] = 0
        else:
            arr[i][j] -= temp[(i, j)]

    part = 0
    visited = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 or visited[i, j]:
                continue
            else:
                stack = deque([])
                stack.append([i, j])
                visited[i, j] = 1

                while stack:
                    for _ in range(len(stack)):
                        a, b = stack.popleft()
                        for k in range(4):
                            y = a + dy[k]
                            x = b + dx[k]
                            if 0 <= y < n and 0 <= x < m and arr[y][x] != 0 and not visited[y, x]:
                                visited[y, x] = 1
                                stack.append([y, x])

                part += 1

    if part == 0:
        answer = 0
        break

    if part >= 2:
        break

print(answer)
