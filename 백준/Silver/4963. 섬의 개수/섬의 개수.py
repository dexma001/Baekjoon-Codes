# 4963

import sys
sys.setrecursionlimit(2**31-1)


def dfs(i, j):
    visited[i][j] = 1
    dw = [0, 1, 1, 1, 0, -1, -1, -1]
    dh = [1, 1, 0, -1, -1, -1, 0, 1]

    for x in range(8):
        p = i + dh[x]
        q = j + dw[x]
        if 1 <= p <= h and 1 <= q <= w and arr[p][q] == 1 and visited[p][q] == 0:
            dfs(p, q)
    return


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [[0]*(w+1)]
    for _ in range(h):
        temp = [0] + list(map(int, input().split()))
        arr.append(temp)

    visited = list(list(0 for _ in range(w+1))for _ in range(h+1))
    answer = 0

    for i in range(1, h+1):
        for j in range(1, w+1):
            if visited[i][j] == 1:
                continue

            if arr[i][j] == 1:
                dfs(i, j)

                answer += 1

    print(answer)
