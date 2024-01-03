# 17404

import sys
input = sys.stdin.readline
ans = 10e8

n = int(input())
li = list()
for _ in range(n):
    li.append(list(map(int, input().split())))

for i in range(3):
    dp = [[ans, ans, ans] for _ in range(n)]
    dp[0][i] = li[0][i]
    for j in range(1, n):
        dp[j][0] = li[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = li[j][1] + min(dp[j-1][2], dp[j-1][0])
        dp[j][2] = li[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])
print(ans)
