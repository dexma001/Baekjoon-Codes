# 23843

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

total = [0] * m

idx = 0
for i in range(n):
    if idx == 0:
        total[idx] += arr[i]
        idx = (idx+1) % m
        continue

    total[idx] += arr[i]
    if total[idx] == total[idx-1]:
        idx = (idx+1) % m

print(total[0])
