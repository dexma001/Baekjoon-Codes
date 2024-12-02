# 1562

n = int(input())
dp = list(list(list(0 for _ in range(1 << 10))
          for _ in range(10)) for _ in range(n))

mod = 1000000000

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(1, n):
    for k in range(10):
        for bit in range(1024):
            if k - 1 >= 0:
                dp[i][k][bit | (1 << k)] += dp[i-1][k-1][bit]
            if k+1 <= 9:
                dp[i][k][bit | (1 << k)] += dp[i-1][k+1][bit]
            dp[i][k][bit | (1 << k)] %= mod

answer = 0
for j in range(10):
    answer += dp[n-1][j][1023]
    answer %= mod

print(answer)
