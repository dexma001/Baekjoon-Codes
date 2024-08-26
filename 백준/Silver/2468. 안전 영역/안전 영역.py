# 2468

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
total_high = set([])

for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    temp = set(temp)
    total_high = total_high.union(temp)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
total_high = list(total_high)
total_high.sort()

answer = 1
for k in range(len(total_high)-1):
    visited = list(list(False for _ in range(n)) for _ in range(n))
    temp_answer = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= total_high[k] or visited[i][j]:
                continue
            else:
                stack = list()
                stack.append([i, j])
                visited[i][j] = True

                while stack:
                    for _ in range(len(stack)):
                        p, q = stack.pop(0)
                        for r in range(4):
                            x = p + dy[r]
                            y = q + dx[r]
                            if 0 <= x < n and 0 <= y < n and arr[x][y] > total_high[k] and not visited[x][y]:
                                visited[x][y] = True
                                stack.append([x, y])
                temp_answer += 1
    answer = max(answer, temp_answer)

print(answer)
