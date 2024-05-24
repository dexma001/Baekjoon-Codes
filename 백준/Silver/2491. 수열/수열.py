# 2491

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list([0] * (n+1) for _ in range(2))
dp[0][1] = 1
dp[1][1] = 1

answer = max(dp[0][1], dp[1][1])
for i in range(2, n+1):
    if arr[i] > arr[i-1]:
        dp[0][i] = dp[0][i-1] + 1
        dp[1][i] = 1
    elif arr[i] < arr[i-1]:
        dp[0][i] = 1
        dp[1][i] = dp[1][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1] + 1
        dp[1][i] = dp[1][i-1] + 1
    answer = max(answer, dp[0][i], dp[1][i])

print(answer)
