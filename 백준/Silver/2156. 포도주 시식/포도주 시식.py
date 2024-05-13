# 2156

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = list([0] * (n+1) for _ in range(4))
dp[0][1] = arr[1]
dp[1][1] = arr[1]

for i in range(2, n+1):
    if i == 2:
        dp[0][i] = dp[0][i-1] + arr[i]
        dp[1][i] = arr[2]
        dp[2][i] = arr[1]

    else:
        dp[0][i] = dp[1][i-1] + arr[i]
        dp[1][i] = max(dp[2][i-1], dp[3][i-1]) + arr[i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
        dp[3][i] = max(dp[2][i-1], dp[3][i-1])

print(max(dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1]))
