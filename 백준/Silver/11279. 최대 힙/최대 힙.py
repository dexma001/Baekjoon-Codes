# 11279

import heapq
import sys
input = sys.stdin.readline

arr = list()
for _ in range(int(input())):
    temp = int(input())
    if temp == 0:
        if len(arr) == 0:
            print(0)
        else:
            a, b = heapq.heappop(arr)
            print(b)
    else:
        heapq.heappush(arr, (-temp, temp))
