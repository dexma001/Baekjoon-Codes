# 2667

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

visited = list(list(False for _ in range(n)) for _ in range(n))
answer = list()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0 or visited[i][j]:
            continue
        else:
            temp_answer = 0
            stack = list()
            stack.append([i, j])
            visited[i][j] = True

            while stack:
                for _ in range(len(stack)):
                    temp_answer += 1
                    a, b = stack.pop(0)
                    for k in range(4):
                        x = a + dx[k]
                        y = b + dy[k]

                        if 0 <= x < n and 0 <= y < n and arr[x][y] == 1 and not visited[x][y]:
                            visited[x][y] = True
                            stack.append([x, y])
            answer.append(temp_answer)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
