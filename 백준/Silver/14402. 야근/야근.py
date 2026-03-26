#14402

import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = defaultdict(int)

answer = 0

for _ in range(n):
    s, p = map(str, input().split())
    
    if p == "+":
        if arr[s]:
            arr[s] += 1
        else:
            arr[s] = 1
    else:
        if arr[s]:
            arr[s] -= 1
        else:
            answer += 1

for i, j in enumerate(arr):
    if arr[j]:
        answer += arr[j]

print(answer)