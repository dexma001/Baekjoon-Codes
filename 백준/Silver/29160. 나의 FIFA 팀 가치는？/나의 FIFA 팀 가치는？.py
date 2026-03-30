#29160

import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

n, k = map(int, input().split())
arr = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(arr[a], (-b, b))

for _ in range(k):
    for i in list(arr.keys()):
        _, temp = heapq.heappop(arr[i])
        heapq.heappush(arr[i], (-temp+1, temp-1))

answer = 0


for i in list(arr.keys()):
    answer += heapq.heappop(arr[i])[1]

print(answer)