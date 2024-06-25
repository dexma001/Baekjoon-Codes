# 5569

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = list(list([0, 0, 0, 0] for _ in range(n+1))
          for _ in range(m+1))  # 오오/위오/오위/위위

for i in range(1, m+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            continue

        if i == 1 or j == 1:
            if i == 1:
                dp[i][j] = [1, 0, 0, 0]
            else:
                dp[i][j] = [0, 0, 0, 1]

        else:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][1] = dp[i][j-1][3]
            dp[i][j][2] = dp[i-1][j][0]
            dp[i][j][3] = dp[i-1][j][2] + dp[i-1][j][3]

print(sum(dp[m][n]) % 100000)
