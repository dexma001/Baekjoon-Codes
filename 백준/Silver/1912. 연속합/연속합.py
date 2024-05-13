# 1912

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = list([0] * n for _ in range(2))

dp[0][0] = arr[0]
dp[1][0] = arr[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+arr[i], dp[1][i-1]+arr[i])

    dp[1][i] = arr[i]

print(max(max(dp[0]), max(dp[1])))
