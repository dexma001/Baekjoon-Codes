# 2670

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = float(input())
    dp[i] = max(dp[i], dp[i] * dp[i-1])


print('%.3f' % max(dp))
