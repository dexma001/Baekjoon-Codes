# 2225

n, m = map(int, input().split())
dp = list([0] * (n+1) for _ in range(m+1))

for i in range(0, n+1):
    dp[1][i] = 1

for i in range(2, m+1):
    for j in range(0, n+1):
        if j == 0:
            dp[i][j] = 1
        else:
            for k in range(0, j+1):
                dp[i][j] += dp[i-1][k]

print(dp[m][n] % 1000000000)
