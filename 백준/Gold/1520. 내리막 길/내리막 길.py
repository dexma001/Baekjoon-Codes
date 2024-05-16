# 1520

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

x = [-1, 0, 0, 1]
y = [0, -1, 1, 0]

dp = list(list(-1 for _ in range(m+1)) for _ in range(n+1))


def dynamic(i, j):
    if i == n and j == m:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    temp = 0
    for k in range(4):
        dx = i + x[k]
        dy = j + y[k]
        if 1 <= dx <= n and 1 <= dy <= m and arr[dx][dy] < arr[i][j]:
            temp += dynamic(dx, dy)
    dp[i][j] = temp
    return dp[i][j]


print(dynamic(1, 1))
