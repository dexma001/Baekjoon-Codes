# 2293

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (m+1)

for _ in range(n):
    a = int(input())
    if a > m:
        continue
    dp[a] += 1
    temp = a+1
    while temp <= m:
        dp[temp] += dp[temp-a]
        temp += 1

print(dp[-1])
