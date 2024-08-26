# 2583

import sys
input = sys.stdin.readline

m, n, k = list(map(int, input().split()))
arr = list(list(0 for _ in range(n)) for _ in range(m))

for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited = list(list(False for _ in range(n)) for _ in range(m))
answer = list()

for p in range(m):
    for q in range(n):
        if arr[p][q] == 1 or visited[p][q]:
            continue
        else:
            stack = list()
            stack.append([p, q])
            visited[p][q] = True
            temp_answer = 1

            while stack:
                for _ in range(len(stack)):
                    p1, q1 = stack.pop(0)
                    for k in range(4):
                        y = p1 + dy[k]
                        x = q1 + dx[k]
                        if 0 <= y < m and 0 <= x < n and arr[y][x] == 0 and not visited[y][x]:
                            visited[y][x] = True
                            temp_answer += 1
                            stack.append([y, x])

            answer.append(temp_answer)

answer.sort()
print(len(answer))
print(*answer)
