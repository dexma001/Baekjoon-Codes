# 2748

dp = [0, 1]

n = int(input())
if n <= 1:
    print(dp[n])
else:
    for i in range(n-1):
        dp.append(dp[-1] + dp[-2])

    print(dp[-1])
