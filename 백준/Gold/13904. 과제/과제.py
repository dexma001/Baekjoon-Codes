# 13904

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    heapq.heappush(arr, list(map(int, input().split())))

answer = list()
i = 1
while arr:
    temp = heapq.heappop(arr)
    if temp[0] >= i:
        heapq.heappush(answer, temp[1])
        i += 1
    else:
        heapq.heappop(answer)
        heapq.heappush(answer, temp[1])

print(sum(answer))
