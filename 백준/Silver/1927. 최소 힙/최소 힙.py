# 1927

import sys
import heapq
input = sys.stdin.readline

heap_list = list()

for _ in range(int(input())):
    det = int(input())
    if det == 0:
        if len(heap_list) == 0:
            print(0)
        else:
            a = heapq.heappop(heap_list)
            print(a)
    else:
        heapq.heappush(heap_list, det)
