# 27111

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = defaultdict(int)

answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    if b == 1:
        if arr[a] == 0:
            arr[a] = 1
        else:
            answer += 1
    else:
        if arr[a] == 1:
            arr[a] = 0
        else:
            answer += 1

for i in arr.keys():
    if arr[i] != 0:
        answer += 1

print(answer)
