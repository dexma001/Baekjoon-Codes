# 1720

import sys
input = sys.stdin.readline

dp = list(0 for _ in range(31))

dp[0] = 1
dp[1] = 1

for i in range(2, 31):
    dp[i] = dp[i-1] + 2*dp[i-2]

n = int(input())
if n % 2 == 0:
    print((dp[n] + dp[n//2] + 2*dp[(n-2)//2])//2)
else:
    print((dp[n] + dp[(n-1)//2])//2)
