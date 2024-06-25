# 1563

import sys
input = sys.stdin.readline

dp = list([0] * 1001 for _ in range(3))

dp[0][1] = 1
dp[1][1] = 1
dp[2][1] = 1

dp[0][2] = 3
dp[1][2] = 2
dp[2][3] = 3

dp[0][3] = 8
dp[1][3] = 4
dp[2][3] = 7

for i in range(4, 1001):
    dp[0][i] = dp[0][i-1] + dp[1][i-1] + dp[2][i-1]
    dp[1][i] = dp[1][i-1] + dp[1][i-2] + dp[1][i-3]
    dp[2][i] = dp[0][i-1] + dp[1][i-1] + dp[0][i-2] + dp[1][i-2]

n = int(input())
print((dp[0][n] + dp[1][n] + dp[2][n]) % 1000000)
