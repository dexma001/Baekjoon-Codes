# 2169

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (m+1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    arr.append(temp)

dp = list([0] * (m+1) for _ in range(n+1))

dp[1][1] = arr[1][1]
for i in range(2, m+1):
    dp[1][i] = dp[1][i-1] + arr[1][i]

for i in range(2, n+1):
    l = [0] * (m+1)
    r = [0] * (m+1)

    l[1] = dp[i-1][1] + arr[i][1]
    r[m] = dp[i-1][m] + arr[i][m]

    for j in range(2, m+1):
        l[j] = max(dp[i-1][j], l[j-1]) + arr[i][j]
        r[-j] = max(dp[i-1][-j], r[-j+1]) + arr[i][-j]

    dp[i] = list(max(ll, rr) for ll, rr in zip(l, r))

print(dp[n][m])
