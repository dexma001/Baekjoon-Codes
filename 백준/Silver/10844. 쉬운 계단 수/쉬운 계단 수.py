# 10844

import sys
input = sys.stdin.readline

dp = list([0] * 101 for _ in range(10))

for i in range(10):
    if i == 0:
        continue
    dp[i][1] = 1


for j in range(2, 101):
    for i in range(10):
        if i == 0:
            dp[i][j] = dp[i+1][j-1]
        elif i == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]


n = int(input())
answer = 0
for i in range(10):
    answer += dp[i][n]

print(answer % 1000000000)
