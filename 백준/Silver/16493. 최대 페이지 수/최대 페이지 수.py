# 16493

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])

dp = list(list(0 for _ in range(n+1)) for _ in range(m+1))

for i in range(1, m+1):
    for j in range(1, n+1):
        if j < arr[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], arr[i-1][1] + dp[i-1][j-arr[i-1][0]])

print(max(dp[-1]))
