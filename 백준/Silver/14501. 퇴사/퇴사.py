# 14501

import sys
input = sys.stdin.readline

n = int(input())
time = [0]
fee = [0]

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    fee.append(b)

dp = [0] * (n+1)

for i in range(1, n+1):
    if i + time[i] - 1 > n:
        continue
    dp[i+time[i]-1] = max(dp[i+time[i]-1], max(dp[0:i]) + fee[i])

print(max(dp))
