# 25418

import sys
input = sys.stdin.readline

a, k = map(int, input().split())
dp = list(i-a for i in range(a, k+1))

for i in range(a+1, k+1):
    if i % 2 == 0 and i//2 >= a:
        dp[i-a] = min(dp[i-a], dp[i-a-1] + 1, dp[i//2-a] + 1)
    else:
        dp[i-a] = min(dp[i-a-1]+1, dp[i-a])
print(dp[-1])
