# 2591

import sys
input = sys.stdin.readline

arr = [0] + list(map(int, input().rstrip()))
len_n = len(arr)
dp = list([0] * (len_n) for _ in range(2))
dp[0][1] = 1
dp[1][1] = 0

for i in range(2, len_n):
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
    if arr[i] == 0:
        dp[0][i] = 0
        dp[1][i] = dp[0][i-1]

    elif 1 <= int(str(arr[i-1]) + str(arr[i])) <= 34:
        dp[1][i] = dp[0][i-1]

print(dp[0][-1] + dp[1][-1])
