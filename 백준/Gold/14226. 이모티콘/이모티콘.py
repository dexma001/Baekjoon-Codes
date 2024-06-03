# 14226

n = int(input())

dp = [0, 0] + list(i for i in range(2, 2*n+1))

for i in range(2, 2*n+1//2 + 1):
    copy = 1
    for j in range(i*2, 2*n+1, i):
        dp[j] = min(dp[j], dp[i] + copy + ((j-i)//i))
        for k in range(j-1, j-i-1, -1):
            dp[k] = min(dp[k], dp[j] + (j-k))

print(dp[n])
