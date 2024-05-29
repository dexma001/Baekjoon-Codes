# 16395

import sys
input = sys.stdin.readline

dp = list([0]*i for i in range(1, 31))

dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, 30):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

n, m = map(int, input().split())
print(dp[n-1][m-1])
