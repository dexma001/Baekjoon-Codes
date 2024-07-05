# 10835

import sys
input = sys.stdin.readline

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

dp = list(list(0 for _ in range(n+1)) for _ in range(n+1))

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if left[i] > right[j]:
            dp[i][j] = dp[i][j+1] + right[j]
        else:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])

print(dp[0][0])
