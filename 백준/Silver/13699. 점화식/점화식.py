# 13699

dp = [0] * 36
dp[0] = 1
dp[1] = 1

for i in range(2, 36):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[int(input())])
