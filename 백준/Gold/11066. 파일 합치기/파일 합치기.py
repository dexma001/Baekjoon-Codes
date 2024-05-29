# 11066

import sys
input = sys.stdin.readline

m = int(input())

for _ in range(m):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = list([0] * (n) for _ in range(n))

    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        for j in range(i+2, n):
            dp[i][j] = dp[i][j-1] + arr[j]

    for i in range(2, n):
        for j in range(n-i):
            k = i + j
            temp = list(dp[j][x] + dp[x+1][k] for x in range(j, k))
            dp[j][k] += min(temp)

    print(dp[0][-1])
