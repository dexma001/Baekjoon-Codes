# 13305

import sys
input = sys.stdin.readline

n = int(input())
length = [0] + list(map(int, input().split()))
value = list(map(int, input().split()))


minor = value[0]
dp = list(0 for _ in range(n))
dp[0] = minor*length[1]

for i in range(1, n-1):
    if value[i] < minor:
        minor = value[i]
    dp[i] = dp[i-1] + length[i+1]*minor

print(dp[-2])
