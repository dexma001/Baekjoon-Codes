# 5557

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = list([0] * (n+1) for _ in range(21))

dp[arr[1]][1] = 1

for i in range(2, n):
    for j in range(21):
        if j+arr[i] > 20:
            pass
        else:
            dp[j+arr[i]][i] += dp[j][i-1]

        if j-arr[i] < 0:
            pass
        else:
            dp[j-arr[i]][i] += dp[j][i-1]

print(dp[arr[-1]][-2])
