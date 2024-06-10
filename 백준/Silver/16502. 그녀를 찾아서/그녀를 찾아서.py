# 16502

import sys
from collections import defaultdict
input = sys.stdin.readline

time = int(input())
n = int(input())
arr = defaultdict(list)
for _ in range(n):
    a, b, c = map(str, input().split())
    arr[b].append((a, float(c)))

dp = list([0, 0, 0, 0] for _ in range(time+1))
dp[0] = [0.25, 0.25, 0.25, 0.25]

for i in range(1, time+1):
    for j in range(4):
        for a, b in arr[chr(j+65)]:
            a1 = ord(a) - 65
            dp[i][j] += dp[i-1][a1] * b

for i in range(4):
    print(dp[-1][i] * 100)
