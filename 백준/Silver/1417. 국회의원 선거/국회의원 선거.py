# 1417

import heapq
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
dasom = [-t, t]

arr = list()
for _ in range(n-1):
    k = int(input())
    heapq.heappush(arr, [-k, k])

answer = 0

while arr and arr[0][1] >= dasom[1]:
    a, b = heapq.heappop(arr)
    dasom[0] -= 1
    dasom[1] += 1
    heapq.heappush(arr, [a+1, b-1])
    answer += 1

print(answer)
