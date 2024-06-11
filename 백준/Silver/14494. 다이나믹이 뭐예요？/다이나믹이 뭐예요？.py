# 14494

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = list(list([0, 0, 0] for _ in range(m+1)) for _ in range(n+1))
dp[1][1] = [1, 0, 0]

x = [0, -1, -1]
y = [-1, 0, -1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            continue
        for k in range(3):
            dx = i + x[k]
            dy = j + y[k]
            if 1 <= dx <= n and 1 <= dy <= m:
                dp[i][j][k] = sum(dp[dx][dy]) % 1000000007

print(sum(dp[-1][-1]) % 1000000007)
