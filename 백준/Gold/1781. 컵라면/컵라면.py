# 1781

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(0 for _ in range(n))

for i in range(n):
    arr[i] = list(map(int, input().split()))

arr.sort(key=lambda x: [x[0], x[1]])

answer_arr = list()

for a, b in arr:
    heapq.heappush(answer_arr, b)
    if a < len(answer_arr):
        heapq.heappop(answer_arr)

print(sum(answer_arr))
