# 27210

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

dp1 = list(0 for _ in range(n+1))
dp2 = list(0 for _ in range(n+1))

if arr[1] == 1:
    dp1[1] = 1

for i in range(2, n+1):
    if arr[i] == 1:
        dp1[i] = dp1[i-1] + 1
    else:
        if dp1[i-1] > 0:
            dp1[i] = dp1[i-1] - 1
        else:
            continue

if arr[1] == 2:
    dp2[1] = 1

for j in range(2, n+1):
    if arr[j] == 2:
        dp2[j] = dp2[j-1] + 1
    else:
        if dp2[j-1] > 0:
            dp2[j] = dp2[j-1] - 1
        else:
            continue

print(max(max(dp1), max(dp2)))
