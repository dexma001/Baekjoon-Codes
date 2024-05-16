# 1699

import math

n = int(input())
dp = list(i for i in range(n+1))

for i in range(2, math.floor(math.sqrt(n))+1):
    temp = i**2
    dp[temp] = 1
    for j in range(temp+1, (i+1)**2):
        if j > n:
            break
        for k in range(2, math.floor(math.sqrt(j))+1):
            dp[j] = min(dp[j], dp[j-k**2]+1)

print(dp[-1])
