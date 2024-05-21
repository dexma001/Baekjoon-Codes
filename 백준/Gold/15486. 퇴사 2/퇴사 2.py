# 15486

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = list([0] * (n+1) for _ in range(2))


for i in range(1, n+1):
    dp[0][i] = max(dp[0][i], dp[1][i-1])
    a, b = arr[i]
    if i + a > n+1:
        pass
    else:
        dp[1][i+a-1] = max(dp[1][i+a-1], dp[0][i] + b)

    dp[1][i] = max(dp[1][i], dp[0][i])

print(dp[1][-1])
