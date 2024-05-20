# 1965

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

answer = 0

for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
        answer = dp[1]
    else:
        for j in range(i-1, 0, -1):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
                answer = max(answer, dp[i])
            if dp[i] == 0:
                dp[i] = 1

print(answer)
