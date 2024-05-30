# 1475

import sys
import math
input = sys.stdin.readline

temp = list(map(int, input().rstrip()))
dp = [0] * 10

for i in temp:
    if i == 6 or i == 9:
        dp[6] += 1
        dp[9] += 1
    else:
        dp[i] += 1

answer = 0
for i in range(len(dp)):
    if i == 6 or i == 9:
        answer = max(answer, math.ceil(dp[i]/2))
    else:
        answer = max(answer, dp[i])

print(answer)
