from decimal import *
getcontext().rounding = ROUND_HALF_UP

n, m = map(int, input().split())
arr = list(map(float, input().split()))

dp = list(list(0 for _ in range(n+1)) for _ in range(2))

if m == 1:
    dp[1][0] = m
else:
    dp[0][0] = 1

for i in range(1, n+1):
    dp[0][i] = dp[0][i-1] * arr[0] + dp[1][i-1] * arr[2]
    dp[1][i] = dp[0][i-1] * arr[1] + dp[1][i-1] * arr[3]

print(int(round(Decimal(dp[0][-1] * 1000), 0)))
print(int(round(Decimal(dp[1][-1] * 1000), 0)))