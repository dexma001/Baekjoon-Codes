# 1915

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[-1] * (m+1)]
for _ in range(n):
    arr.append([-1] + list(map(int, list(input().rstrip()))))

dp = list([0] * (m+1) for _ in range(n+1))

answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] != 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            answer = max(answer, dp[i][j])

print(answer**2)
