# 2718

import sys
input = sys.stdin.readline

arr = list()
for _ in range(int(input())):
    arr.append(int(input()))

t = max(arr)+1
dp = list(list(0 for _ in range(t)) for _ in range(5))

dp[4][0] = 1
dp[0][1] = 1
dp[1][1] = 1
dp[2][1] = 1
dp[4][1] = 1
for i in range(2, t):
    dp[0][i] = dp[4][i-1] + dp[1][i-1]
    dp[1][i] = dp[4][i-1] + dp[0][i-1]
    dp[2][i] = dp[4][i-1] + dp[3][i-1]
    dp[3][i] = dp[2][i-1]
    dp[4][i] = dp[4][i-1] + dp[0][i-1] + dp[1][i-1] + dp[2][i-1] + dp[4][i-2]

for i in arr:
    print(dp[4][i])
