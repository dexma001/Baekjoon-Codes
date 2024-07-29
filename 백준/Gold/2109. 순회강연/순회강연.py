# 2109

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split()))for _ in range(n))
arr.sort(key=lambda x: x[1])

answer = list()
date = 0

for a, b in arr:
    heapq.heappush(answer, a)
    date += 1

    if date > b:
        heapq.heappop(answer)
        date -= 1

print(sum(answer))
