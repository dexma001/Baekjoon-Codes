# 9507

import sys
input = sys.stdin.readline

dp = [1] * 69
dp[2] = 2
dp[3] = 4

for i in range(4, 69):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

n = int(input())
for _ in range(n):
    print(dp[int(input())])
