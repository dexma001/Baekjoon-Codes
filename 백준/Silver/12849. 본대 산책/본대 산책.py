# 12849

arr = [[1, 2], [0, 3, 2], [0, 1, 3, 4], [1, 2, 4, 5],
       [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]

n = int(input())

dp = list(list(0 for _ in range(n+1)) for _ in range(8))
dp[0][0] = 1

for k in range(1, n+1):
    for i in range(8):
        for j in arr[i]:
            dp[i][k] += dp[j][k-1]
            dp[i][k] %= 1000000007

print(dp[0][n])
