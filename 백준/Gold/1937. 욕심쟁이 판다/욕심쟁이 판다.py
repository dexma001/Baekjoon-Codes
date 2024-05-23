# 1937

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 ** 31-1)

n = int(input())
arr = [[0] * (n+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

dp = list([0] * (n+1) for _ in range(n+1))
x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]


def dfs(a, b):
    if dp[a][b] != 0:
        return
    else:
        dp[a][b] = 1
        for i in range(4):
            dx = a + x[i]
            dy = b + y[i]
            if 1 <= dx <= n and 1 <= dy <= n and arr[dx][dy] > arr[a][b]:
                dfs(dx, dy)
                dp[a][b] = max(dp[a][b], 1+dp[dx][dy])


answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] != 0:
            continue
        else:
            dfs(i, j)
            answer = max(answer, dp[i][j])

print(answer)
