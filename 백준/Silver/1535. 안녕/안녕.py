# 1535

import sys
input = sys.stdin.readline

n = int(input())
hp = [0] + list(map(int, input().split()))
pleasure = [0]+list(map(int, input().split()))

dp = list([0] * (101) for _ in range(n+1))

for i in range(1, n+1):
    for j in range(1, 101):
        if hp[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i]] + pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
