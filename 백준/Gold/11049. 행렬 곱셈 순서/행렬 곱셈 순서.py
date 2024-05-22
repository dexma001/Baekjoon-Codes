# 11049

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = list([0] * (n+1) for _ in range(n+1))

for i in range(1, n):
    for j in range(1, n-i+1):
        dp[j][i+j] = 2 ** 31
        for k in range(j, i+j):
            dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1]
                             [i+j] + (arr[j][0] * arr[k][1] * arr[i+j][1]))

print(dp[1][n])
