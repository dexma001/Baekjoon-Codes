# 7570

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = list(0 for _ in range(n+1))

for i in arr:
    dp[i] = dp[i-1] + 1

print(n - max(dp))
