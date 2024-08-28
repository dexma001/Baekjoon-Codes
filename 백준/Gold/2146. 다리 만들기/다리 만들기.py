# 2146

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

land_outline = defaultdict(int)
visited = list(list(0 for _ in range(n)) for _ in range(n))
land_num = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0 or visited[i][j]:
            continue
        else:
            stack = list()
            stack.append([i, j])
            visited[i][j] = True

            while stack:
                for _ in range(len(stack)):
                    a, b = stack.pop()
                    land_outline[a, b] = land_num
                    is_inner = 0
                    for k in range(4):
                        y = a + dy[k]
                        x = b + dx[k]
                        if 0 <= y < n and 0 <= x < n and arr[y][x]:
                            is_inner += 1
                            if not visited[y][x]:
                                visited[y][x] = 1
                                stack.append([y, x])
                    if a == 0 or a == n-1:
                        if b == 0 or b == n-1:
                            if is_inner == 2 and land_outline[(a, b)]:
                                land_outline.pop((a, b))
                        else:
                            if is_inner == 3 and land_outline[(a, b)]:
                                land_outline.pop((a, b))
                    else:
                        if b == 0 or b == n-1:
                            if is_inner == 3 and land_outline[(a, b)]:
                                land_outline.pop((a, b))
                        else:
                            if is_inner == 4 and land_outline[(a, b)]:
                                land_outline.pop((a, b))

        land_num += 1

answer = 10001

for i, j in list(land_outline):
    stack = deque([])
    stack.append([i, j])
    visited1 = defaultdict(int)
    visited1[i, j] = 1
    which_land = land_outline[(i, j)]
    temp_answer = 0

    while stack:
        trig = 0
        for _ in range(len(stack)):
            a, b = stack.popleft()
            for k in range(4):
                y = a + dy[k]
                x = b + dx[k]
                if 0 <= y < n and 0 <= x < n:
                    if arr[y][x] == 1:
                        if land_outline[(y, x)] == which_land:
                            continue
                        else:
                            trig = 1
                            break
                    else:
                        if not visited1[y, x]:
                            visited1[y, x] = 1
                            stack.append([y, x])

        if trig == 1:
            break
        temp_answer += 1

    if temp_answer != 0:
        answer = min(answer, temp_answer)

print(answer)
