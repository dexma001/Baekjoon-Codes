# 19947

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

dp = list([0]*(11+1))
dp[0] = n
dp[1] = math.floor(n*1.05)
dp[2] = math.floor(dp[1]*1.05)
dp[3] = math.floor(max(dp[2]*1.05, n*1.2))
dp[4] = math.floor(max(dp[3] * 1.05, dp[1]*1.2))

for i in range(5, m+1):
    dp[i] = math.floor(max(dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35))

print(dp[m])
