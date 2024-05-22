# 16194

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list([0] * (n+1) for _ in range(n+1))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1:
            dp[j][i] = dp[j-1][i] + arr[i]
        else:
            if j < i:
                dp[j][i] = dp[j][i-1]
            else:
                dp[j][i] = min(dp[j][i-1], dp[j-i][i] + arr[i])

print(dp[-1][-1])
