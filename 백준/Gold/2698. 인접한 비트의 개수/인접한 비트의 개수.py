#2698

dp = list(list([0, 0] for _ in range(101)) for _ in range(101))
dp[0][1][0] = 1
dp[0][1][1] = 1

for i in range(2, 101):
    dp[0][i][0] = sum(dp[0][i-1])
    dp[0][i][1] = dp[0][i-1][0]

for i in range(1, 101):
    for j in range(i, 101):
        if i == j:
            continue
        elif j == i +1:
            dp[i][j][1] = 1
        else:
            dp[i][j][0] = sum(dp[i][j-1])
            dp[i][j][1] = dp[i-1][j-1][1] + dp[i][j-1][0]


for _ in range(int(input())):
    a,b=map(int, input().split())
    print(sum(dp[b][a]))