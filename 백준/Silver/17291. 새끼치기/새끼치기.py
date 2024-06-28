# 17291

import sys
input = sys.stdin.readline

dp = list(list(0 for _ in range(21)) for _ in range(2))
dp[0][1] = 1
dp[1][1] = 1
dp[0][2] = 2
dp[1][2] = 1
dp[0][3] = 4
dp[1][3] = 2

for i in range(4, 21):
    if i % 2 != 0:
        dp[0][i] = dp[0][i-1] * 2
        dp[1][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1] * 2 - dp[1][i-3] - dp[1][i-4]
        dp[1][i] = dp[0][i-1]

print(dp[0][int(input())])
