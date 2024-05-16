# 2294

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = list(10**8 for _ in range(m+1))

for _ in range(n):
    a = int(input())
    if a > m:
        continue
    dp[a] = 1
    temp = a + 1
    while temp <= m:
        dp[temp] = min(dp[temp], dp[temp-a]+1)
        temp += 1

if dp[-1] != 10**8:
    print(dp[-1])
else:
    print(-1)
