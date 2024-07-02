# 13334

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    arr.append((a, b))
arr.sort(key=lambda x: [x[1], x[0]])
railway = int(input())

heap = list()
answer = 0

for a, b in arr:
    heapq.heappush(heap, a)
    end = b - railway
    while heap and heap[0] < end:
        heapq.heappop(heap)
    answer = max(answer, len(heap))

print(answer)
