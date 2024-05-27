# 15989

import sys
input = sys.stdin.readline

dp = list([0] * 10001 for _ in range(4))
for i in range(0, 10001):
    dp[1][i] = 1

dp[2][2] = 1
dp[2][3] = 1
dp[3][3] = 1

for i in range(4, 10001):
    for j in range(2, 4):
        for k in range(1, j+1):
            dp[j][i] += dp[k][i-j]

for _ in range(int(input())):
    temp = int(input())
    print(dp[1][temp] + dp[2][temp] + dp[3][temp])
