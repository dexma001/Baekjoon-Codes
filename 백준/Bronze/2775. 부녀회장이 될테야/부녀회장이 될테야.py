# 2775

import sys
input = sys.stdin.readline

n = int(input())

dp = list([0] * 14 for _ in range(14))
dp.insert(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for i in range(1, 15):
    for j in range(0, 14):
        dp[i][j] = sum(dp[i-1][0:j+1])

for _ in range(n):
    a = int(input())
    b = int(input())
    print(dp[a][b-1])
