# 11052

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = list([0] * (n+1) for _ in range(n+1))
max_dp = list(0 for _ in range(n+1))
dp[1] = [0] + [arr[1]] * n
max_dp[1] = max(dp[1])

for i in range(2, n+1):
    for j in range(1, n+1):
        if j == 1:
            dp[i][j] = arr[j] * i
            max_dp[i] = dp[i][j]
        elif j <= i:
            for k in range(0, j//2+1):
                if k == 0:
                    dp[i][j] = arr[i]
                else:
                    dp[i][j] = max(dp[i][j], max_dp[i-k] + max_dp[k])
                    max_dp[i] = max(max_dp[i], dp[i][j])
        else:
            dp[i][j] = max_dp[i]

print(max_dp[n])
