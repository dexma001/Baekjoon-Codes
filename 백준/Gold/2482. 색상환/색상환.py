# 2482

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = list(list(0 for _ in range(n+1)) for _ in range(m+1))

dp[1][1] = 1
dp[1][2] = 2
dp[1][3] = 3

for i in range(4, n+1):
    for j in range(1, m+1):
        if j > i//2:
            dp[j][i] = 0
        else:
            if j == 1:
                dp[j][i] = i
            else:
                dp[j][i] = (dp[j][i-1] + dp[j-1][i-2]) % 1000000003

print(dp[m][n])
