#13549

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

if n>= m:
    print(n-m)

else:
    dijk = list(10**8 for _ in range(100001))
    stack = list()
    heapq.heappush(stack, (0, n))

    while stack:
            a, b = heapq.heappop(stack)
            if dijk[b] != 10**8:
                continue
            dijk[b] = a
            if 0<=b+1<=100000:
                heapq.heappush(stack, (a+1, b+1))
            if 0<=b-1<=100000:
                heapq.heappush(stack, (a+1, b-1))
            if 0<=b*2<=100000:
                heapq.heappush(stack, (a, b*2))
                
    print(dijk[m])