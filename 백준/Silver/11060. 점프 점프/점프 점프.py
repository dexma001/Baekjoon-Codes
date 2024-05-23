# 11060

import sys
input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))
dp = list((0) for _ in range(n+1))
for i in range(1, arr[1]+1):
    dp[1+i] = 1


for i in range(2, n+1):
    if arr[i] == 0 or dp[i] == 0:
        continue
    for j in range(1, arr[i]+1):
        if i + j > n:
            continue

        if dp[i+j] == 0:
            dp[i+j] = dp[i] + 1
        else:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if n == 1:
    print(0)
elif dp[-1] == 0:
    print(-1)
else:
    print(dp[-1])
