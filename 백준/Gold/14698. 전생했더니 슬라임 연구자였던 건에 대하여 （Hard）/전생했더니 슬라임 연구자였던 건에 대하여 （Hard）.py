# 14698

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 1

    heapq.heapify(arr)
    while n > 1:
        k = heapq.heappop(arr)
        p = heapq.heappop(arr)

        answer = (answer*k*p) % 1000000007
        heapq.heappush(arr, k*p)
        n -= 1

    print(answer)
