# 20116

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

det = 0
temp = 0
for i in range(0, n-1):
    if det == 1:
        break
    temp += arr[n-1-i]
    if arr[n-1-i-1]-m < temp/(i+1) < arr[n-1-i-1]+m:
        continue
    else:
        det = 1

if det == 1:
    print('unstable')
else:
    print('stable')
