# 1106

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
arr = list()

for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
arr.sort(key=lambda x: x[1])


INF = 10**9
dp = [0] + list(INF for _ in range(c+100))

for a, b in arr:
    for i in range(1, c+101):
        if i-b > -1:
            dp[i] = min(dp[i], dp[i-b] + a)

print(min(dp[c:c+101]))
