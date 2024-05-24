# 2302

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)
dp = [0] * (n+1)

vip = int(input())
vip_arr = list()

for _ in range(vip):
    temp = int(input())
    arr[temp] = -1
    dp[temp] = 1
    vip_arr.append(temp)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if arr[i] == -1:
        continue
    else:
        if arr[i-1] == -1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + dp[i-2]

answer = 1
for i in vip_arr:
    answer *= dp[i-1]
print(answer*dp[-1])
