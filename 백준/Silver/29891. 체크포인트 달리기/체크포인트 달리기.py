# 29891

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(int(input()))
arr.sort()

answer = 0
while arr:
    answer += abs(arr[-1]) * 2
    for _ in range(m):
        if arr:
            arr.pop()

print(answer)
