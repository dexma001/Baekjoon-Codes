# 2226

import sys
input = sys.stdin.readline

dp = list(0 for _ in range(1001))
dp[1] = 0
dp[2] = 1
dp[3] = 1


for i in range(4, 1001):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[int(input())])
