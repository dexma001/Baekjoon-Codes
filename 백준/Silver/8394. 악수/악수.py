# 8394

import sys
input = sys.stdin.readline

dp = [0] * 10000001

dp[1] = 1
dp[2] = 2
for i in range(3, 10000001):
    dp[i] = (dp[i-1] + dp[i-2]) % 10

print(dp[int(input())])
