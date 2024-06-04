# 4811

import sys
import math
input = sys.stdin.readline

dp = [0] * 31

for i in range(1, 31):
    dp[i] = math.factorial(2*i) // (math.factorial(i) * math.factorial(i+1))

answer = list()
while True:
    n = int(input())
    if n == 0:
        break
    answer.append(dp[n])

for i in answer:
    print(i)
