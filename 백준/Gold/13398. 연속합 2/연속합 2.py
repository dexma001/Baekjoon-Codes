# 13398

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list([0] * (n+1) for _ in range(2))
dp[0][1] = arr[1]

answer = arr[1]
for i in range(2, n+1):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
    answer = max(answer, dp[0][i], dp[1][i])

print(answer)
