# 1932

import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
dp = list([0] * (i) for i in range(1, n+1))
dp[0] = arr[0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == len(arr[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])

print(max(dp[-1]))
