# 11286

import sys
import heapq
input = sys.stdin.readline

heap_list = list()

for _ in range(int(input())):
    a = int(input())
    if a == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            a, b = heapq.heappop(heap_list)
            print(b)
    else:
        list = [abs(a), a]
        heapq.heappush(heap_list, list)
