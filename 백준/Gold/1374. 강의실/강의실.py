# 1374

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort(key=lambda x: (x[1], x[2]))

temp = list()
answer = 0

for i in arr:
    if not temp:
        heapq.heappush(temp, i[2])
        answer += 1
        continue

    if i[1] >= temp[0]:
        heapq.heappop(temp)
        heapq.heappush(temp, i[2])

    else:
        heapq.heappush(temp, i[2])
        answer += 1

print(answer)
