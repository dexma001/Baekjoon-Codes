# 1933

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    l, h, r = map(int, input().split())
    arr.append([l, -h, r])
    arr.append([r, 0, 0])

arr.sort()

answer = list()
heap = [[0, float('inf')]]
peak = 0

for start, height, end in arr:
    if height:
        heapq.heappush(heap, [height, end])
    else:
        while heap and heap[0][1] <= start:
            heapq.heappop(heap)

    ch = -heap[0][0]
    if peak != ch:
        answer.extend([start, ch])
        peak = ch

print(*answer)
