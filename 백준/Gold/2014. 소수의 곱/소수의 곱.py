# 2014

import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))
temp = list()

for i in arr:
    heapq.heappush(temp, i)

for _ in range(n-1):
    t = heapq.heappop(temp)

    for i in arr:
        tt = t * i
        heapq.heappush(temp, tt)
        if not t % i:
            break

print(heapq.heappop(temp))
