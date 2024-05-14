# 1904

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())

dp = [0, 1]

for i in range(1, n+1):
    dp.append((dp[-1] + dp[-2]) % 15746)
print(dp[-1])
