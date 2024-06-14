# 20500

dp = list([0] * 1516 for _ in range(3))
dp[0][1] = 0
dp[1][1] = 1
dp[2][1] = 0

for i in range(2, 1516):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1]) % 1000000007
    dp[1][i] = (dp[0][i-1] + dp[1][i-1]) % 1000000007
    dp[2][i] = (dp[0][i-1] + dp[2][i-1]) % 1000000007

n = int(input())
print(dp[0][n])
