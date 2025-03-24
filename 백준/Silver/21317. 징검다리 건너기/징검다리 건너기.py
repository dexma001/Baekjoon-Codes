# 21317

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
arr.append([0, 0])
for _ in range(n-1):
    arr.append(list(map(int, input().split())))
k = int(input())

dp = list(list(1000000 for _ in range(n+3))
          for _ in range(2))  # 0번째는 k점프 안했을 떄
dp[0][1] = 0
dp[1][1] = 0

for i in range(1, n):
    p, q = arr[i]
    dp[0][i+1] = min(dp[0][i+1], dp[0][i] + p)
    dp[0][i+2] = min(dp[0][i+2], dp[0][i] + q)
    dp[1][i+1] = min(dp[1][i+1], dp[1][i] + p)
    dp[1][i+2] = min(dp[1][i+2], dp[1][i] + q)
    dp[1][i+3] = min(dp[1][i+3], dp[0][i] + k)

print(min(dp[0][n], dp[1][n]))
