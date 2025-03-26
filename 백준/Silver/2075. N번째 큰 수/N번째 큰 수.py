# 2075

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(n-1):
    temp = list(map(int, input().split()))
    for i in temp:
        if i > arr[0]:
            heapq.heappop(arr)
            heapq.heappush(arr, i)

print(arr[0])
