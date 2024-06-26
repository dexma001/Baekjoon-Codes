# 1660

import sys
input = sys.stdin.readline

n = int(input())
num = 0
i = 1

arr = list()
while n > num:
    num += (i*(i+1))//2
    arr.append(num)
    i += 1

dp = list(10**10 for _ in range(n+1))
for i in range(1, n+1):
    for num in arr:
        if num == i:
            dp[i] = 1
            break
        elif num > i:
            break

        dp[i] = min(dp[i], 1+dp[i-num])

print(dp[n])
