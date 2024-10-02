# 1727

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
man = sorted(list(map(int, input().split())))
woman = sorted(list(map(int, input().split())))

dp = list(list(0 for _ in range(n+1)) for _ in range(m+1))

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j-1] + abs(man[j-1] - woman[i-1])
        if i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])
        elif i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])

print(dp[m][n])
