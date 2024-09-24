# 26170

import sys
input = sys.stdin.readline

arr = list()
for _ in range(5):
    arr.append(list(map(int, input().split())))

n, m = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = 10**10


def dfs(n, m, apples, visited, cnt):
    global answer
    if arr[n][m] == 1:
        apples += 1

    if apples == 3:
        answer = min(answer, cnt)
        return

    for i in range(4):
        y = n + dy[i]
        x = m + dx[i]
        if 0 <= y < 5 and 0 <= x < 5:
            if arr[y][x] != -1 and [y, x] not in visited:
                temp = [[y, x]]
                temp.extend(visited)
                dfs(y, x, apples, temp, cnt+1)

    return


dfs(n, m, 0, [[n, m]], 0)
if answer == 10**10:
    print(-1)
else:
    print(answer)
