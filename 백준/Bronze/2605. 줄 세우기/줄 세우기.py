# 2605

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = [1]

for i in range(1, n):
    if arr[i] == 0:
        answer.append(i+1)
    else:
        answer.insert(-arr[i], i+1)

print(*answer)
