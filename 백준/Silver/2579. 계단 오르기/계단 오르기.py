# 2579

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(int(input()) for _ in range(n))

# 0번째 line - 바로 직전 계단을 밟았을 때 / 1번째 line - 바로 직전 계단을 안 밟았을 때
dp = list([0 for _ in range(n+1)] for _ in range(2))
dp[0][1] = arr[1]
dp[1][1] = arr[1]

for i in range(2, n+1):
    dp[0][i] = dp[1][i-1] + arr[i]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + arr[i]

print(max(dp[0][-1], dp[1][-1]))
