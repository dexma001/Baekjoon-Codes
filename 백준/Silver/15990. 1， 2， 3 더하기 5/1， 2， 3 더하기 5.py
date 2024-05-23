# 15990

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**31-1)
mod = 1000000009

n = int(input())
dp = list([0] * 100001 for _ in range(4))
dp[1][1] = 1
dp[2][2] = 1
dp[1][3] = 1
dp[2][3] = 1
dp[3][3] = 1

for i in range(4, 100001):
    dp[1][i] = (dp[2][i-1] + dp[3][i-1]) % mod
    dp[2][i] = (dp[1][i-2] + dp[3][i-2]) % mod
    dp[3][i] = (dp[1][i-3] + dp[2][i-3]) % mod

for _ in range(n):
    m = int(input())
    print((dp[1][m] + dp[2][m] + dp[3][m]) % mod)
