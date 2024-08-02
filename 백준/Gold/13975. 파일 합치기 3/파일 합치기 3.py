# 13975

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    heapq.heapify(arr)

    answer = 0
    while n != 2:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += (a+b)
        heapq.heappush(arr, a+b)
        n -= 1

    answer += sum(arr)
    print(answer)
