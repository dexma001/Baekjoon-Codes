# 2240

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
dp = list([0] * (t+1) for _ in range(w+1))

arr = [0]
for _ in range(t):
    arr.append(int(input()))

for i in range(1, t+1):
    if arr[i] % 2 != 0:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]

    for j in range(1, w+1):
        if arr[i] == 2 and j % 2 != 0:
            dp[j][i] = max(dp[j-1][i-1], dp[j][i-1]) + 1
        elif arr[i] == 1 and j % 2 == 0:
            dp[j][i] = max(dp[j-1][i-1], dp[j][i-1]) + 1
        else:
            dp[j][i] = max(dp[j-1][i-1], dp[j][i-1])

answer = 0
for i in range(w+1):
    answer = max(answer, dp[i][-1])

print(answer)
