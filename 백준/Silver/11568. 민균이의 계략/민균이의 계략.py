# 11568

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list([0] * (n+1) for _ in range(2))
dp[0][1] = 1
dp[1][1] = 0

for i in range(2, n+1):
    dp[0][i] = 1
    for j in range(i-1, 0, -1):
        if arr[i] > arr[j]:
            dp[0][i] = max(dp[0][i], dp[0][j]+1)

    dp[1][i] = max(dp[0][i-1], dp[1][i-1])

print(max(dp[0][-1], dp[1][-1]))
