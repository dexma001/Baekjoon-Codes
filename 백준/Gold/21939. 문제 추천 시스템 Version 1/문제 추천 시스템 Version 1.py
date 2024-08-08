# 21939

import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

heap_small = list()
heap_big = list()

dict_small = defaultdict(int)
dict_big = defaultdict(int)

for _ in range(int(input())):
    a, b = map(int, input().split())
    heapq.heappush(heap_small, (b, a))
    heapq.heappush(heap_big, (-b, -a))

for _ in range(int(input())):
    temp = list(map(str, input().split()))
    if temp[0] == 'add':
        while dict_small[str(heap_small[0][1])] == 1:
            heapq.heappop(heap_small)
        while dict_big[str(heap_big[0][1])] == 1:
            heapq.heappop(heap_big)
        heapq.heappush(heap_small, (int(temp[2]), int(temp[1])))
        heapq.heappush(heap_big, (-int(temp[2]), -int(temp[1])))
        if dict_big[str(-int(temp[1]))] == 1:
            dict_big[str(-int(temp[1]))] = 0
        if dict_small[temp[1]] == 1:
            dict_small[temp[1]] = 0
    elif temp[0] == 'recommend':
        if temp[1] == '-1':
            while dict_small[str(heap_small[0][1])] == 1:
                heapq.heappop(heap_small)
            print(heap_small[0][1])
        else:
            while dict_big[str(heap_big[0][1])] == 1:
                heapq.heappop(heap_big)
            print(-heap_big[0][1])
    else:
        if dict_big[str(-int(temp[1]))] == 0:
            dict_big[str(-int(temp[1]))] = 1
        if dict_small[temp[1]] == 0:
            dict_small[temp[1]] = 1
