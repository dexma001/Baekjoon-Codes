# 17212

import sys
input = sys.stdin.readline

n = int(input())
answer = 0
arr = [1, 2, 5, 7]

dp = list([0] * (n+1) for _ in range(4))

for i in range(4):
    for j in range(1, n+1):
        if i == 0:
            dp[i][j] = dp[i][j-1] + 1

        if j < arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            if j % arr[i] == 0:
                dp[i][j] = j//arr[i]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-arr[i]] +
                               1, dp[i][j-arr[i]]+1)

print(dp[3][n])
