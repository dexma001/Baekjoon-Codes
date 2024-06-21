# 2688

dp = list([0]*10 for _ in range(65))
dp[1] = [1] * 10

for i in range(2, 65):
    for j in range(10):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][k]

for _ in range(int(input())):
    print(sum(dp[int(input())]))
