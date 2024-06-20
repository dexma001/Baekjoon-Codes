# 14728

n, t = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

dp = list(list(0 for _ in range(t+1)) for _ in range(n+1))

for i in range(n+1):
    for j in range(t+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif arr[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], arr[i-1][1] + dp[i-1][j-arr[i-1][0]])
        else:
            dp[i][j] = dp[i-1][j]

print
print(dp[n][t])
