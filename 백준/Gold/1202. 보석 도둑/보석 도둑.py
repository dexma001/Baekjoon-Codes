# 1202

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewel = list()
back_pack = list()
answer = 0

for _ in range(n):
    jewel.append(tuple(map(int, input().split())))
jewel.sort()

for _ in range(k):
    back_pack.append(int(input()))
back_pack.sort()

temp = list()
i = 0
for j in back_pack:
    while i < n and j >= jewel[i][0]:
        heapq.heappush(temp, -jewel[i][1])
        i += 1
    if temp:
        answer += heapq.heappop(temp)

print(-answer)
