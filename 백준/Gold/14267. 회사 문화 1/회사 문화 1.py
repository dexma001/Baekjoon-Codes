# 14267

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = list(0 for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    dp[a] += b

for i in range(2, n+1):
    dp[i] += dp[arr[i]]

print(*dp[1:])
