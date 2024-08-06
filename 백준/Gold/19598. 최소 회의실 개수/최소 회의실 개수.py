# 19598

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

answer = list()
heapq.heappush(answer, arr[0][1])
heapq.heappop(arr)

for i in range(1, n):
    temp = heapq.heappop(arr)
    if temp[0] >= answer[0]:
        heapq.heappop(answer)
    heapq.heappush(answer, temp[1])

print(len(answer))
