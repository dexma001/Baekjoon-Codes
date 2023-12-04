# 27172

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
li = list()

answer = dict()

maxNum = 0

for i, num in enumerate([*map(int, input().strip().split())]):
    maxNum = max(maxNum, num)
    li.append((i, num))
    answer[num] = 0

li.sort(key=lambda x: x[1])

for l in range(n):
    a, b = li[l]

    for target in range(b*2, maxNum+1, b):
        if target in answer:
            answer[b] += 1
            answer[target] -= 1

for key, item in answer.items():
    print(item, end=' ')
