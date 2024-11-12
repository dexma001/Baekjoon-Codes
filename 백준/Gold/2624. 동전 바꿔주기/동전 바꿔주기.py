# 2624

import sys
input = sys.stdin.readline

n = int(input())
dp = list(0 for _ in range(n + 1))
dp[0] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(n, -1, -1):
        j = 1
        while j <= b and i - a*j >= 0:
            dp[i] += dp[i-a*j]
            j += 1

print(dp[n])
