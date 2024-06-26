# 14430

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    arr.append(temp)

dp = list(list(0 for _ in range(m+1)) for _ in range(n+1))
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            dp[i][j] = arr[i][j]
        else:
            if arr[i][j] == 0:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1

print(dp[n][m])
