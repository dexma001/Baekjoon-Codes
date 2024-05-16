# 11051

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = list([0] * (i+1) for i in range(n+1))

for i in range(1, n+1):
    for j in range(0, i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007

print(dp[n][m])
