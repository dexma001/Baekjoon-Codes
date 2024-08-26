# 1012

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = list(list(0 for _ in range(m)) for _ in range(n))
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    visited = list(list(False for _ in range(m)) for _ in range(n))
    answer = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 or visited[i][j]:
                continue
            else:
                stack = list()
                stack.append([i, j])
                visited[i][j] = True

                while stack:
                    for _ in range(len(stack)):
                        a, b = stack.pop(0)
                        for t in range(4):
                            x = a + dx[t]
                            y = b + dy[t]
                            if 0 <= x < n and 0 <= y < m and arr[x][y] == 1 and not visited[x][y]:
                                visited[x][y] = True
                                stack.append([x, y])
                answer += 1
    print(answer)
