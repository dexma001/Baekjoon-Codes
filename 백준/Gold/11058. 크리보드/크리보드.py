# 11058

import sys
input = sys.stdin.readline

dp = list(i for i in range(101))
for i in range(4, 101):
    for j in range(0, i-3):
        dp[i] = max(dp[i], dp[j] * (i-j-1))

print(dp[int(input())])
