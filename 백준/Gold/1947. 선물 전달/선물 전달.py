# 1947

import sys
input = sys.stdin.readline

dp = list([0] * 1000001 for _ in range(2))
dp[0][2] = 1
dp[0][3] = 1
dp[1][3] = 1

for i in range(4, 1000001):
    dp[0][i] = ((i-1) * (dp[0][i-2] + dp[1][i-2])) % 1000000000
    dp[1][i] = ((i-1) * (dp[0][i-1] + dp[1][i-1])) % 1000000000

n = int(input())
print((dp[0][n] + dp[1][n]) % 1000000000)
