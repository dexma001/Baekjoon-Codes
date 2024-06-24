# 14852

import sys
input = sys.stdin.readline

dp = list(0 for _ in range(1000001))
dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, 1000001):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3]) % 1000000007
print(dp[int(input())])
