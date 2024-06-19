# 17069

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*(n+1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    arr.append(temp)

dp = list(list([0, 0, 0] for _ in range(n+1)) for _ in range(n+1))  # 가/세/대
dp[1][2] = [0, 0, 1]
for i in range(3, n+1):
    for j in range(1, n+1):
        if arr[j][i] != 1:
            if arr[j-1][i] != 1:
                dp[j][i][1] = dp[j-1][i][1] + dp[j-1][i][2]
            if arr[j][i-1] != 1:
                dp[j][i][0] = dp[j][i-1][0] + dp[j][i-1][2]
            if arr[j-1][i] != 1 and arr[j][i-1] != 1 and arr[j-1][i-1] != 1:
                dp[j][i][2] = sum(dp[j-1][i-1])

print(sum(dp[n][n]))
