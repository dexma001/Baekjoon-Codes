# 17626

import math

n = int(input())
dp = list([0] * (n+1) for _ in range(5))

m = int(math.sqrt(n))

for i in range(1, m+1):
    dp[1][i*i] = 1

    for j in range(i*i+1, n+1):
        dp[2][j] += dp[1][j-i*i]
        dp[3][j] += dp[2][j-i*i]
        dp[4][j] += dp[3][j-i*i]

answer = 5
for i in range(1, 5):
    if dp[i][n] != 0:
        answer = min(answer, i)

print(answer)
