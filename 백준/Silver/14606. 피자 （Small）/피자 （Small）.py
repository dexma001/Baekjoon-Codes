# 2666

import sys
input = sys.stdin.readline

dp = list(0 for _ in range(11))
dp[1] = 0
dp[2] = 1
dp[3] = 3

for i in range(4, 11):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i-j] + j*(i-j))

print(dp[int(input())])
