# 3067

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    value = int(input())

    dp = list(0 for _ in range(value+1))
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], value+1):
            dp[j] += dp[j-coins[i]]

    print(dp[-1])
