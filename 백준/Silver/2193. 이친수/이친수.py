# 2193

import sys
input = sys.stdin.readline

dp = list([0] * 91 for _ in range(2))
dp[0][1] = 1

for i in range(2, 91):
    dp[0][i] = dp[1][i-1]
    dp[1][i] = dp[0][i-1] + dp[1][i-1]

n = int(input())
print(dp[0][n] + dp[1][n])
