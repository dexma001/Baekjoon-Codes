# 17271

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = list(list(0 for _ in range(n+1)) for _ in range(2))

for i in range(1, n+1):
    if i < m:
        dp[0][i] = 1
    elif i == m:
        dp[0][i] = 1
        dp[1][i] = 1
    else:
        dp[0][i] = dp[0][i-1] + dp[1][i-1]
        dp[1][i] = dp[0][i-m] + dp[1][i-m]

print((dp[0][-1] + dp[1][-1]) % 1000000007)
