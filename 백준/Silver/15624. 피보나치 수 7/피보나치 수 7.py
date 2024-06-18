# 15624

dp = list(0 for _ in range(1000001))
dp[1] = 1

for i in range(2, 1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[int(input())])
