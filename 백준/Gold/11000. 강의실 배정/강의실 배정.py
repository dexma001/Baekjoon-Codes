# 11000

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[0], x[1]])

answer_arr = list()
heapq.heappush(answer_arr, arr[0][1])

answer = 1
for i in range(1, n):
    temp = arr[i]
    if temp[0] < answer_arr[0]:
        heapq.heappush(answer_arr, temp[1])
        answer += 1
    else:
        heapq.heappop(answer_arr)
        heapq.heappush(answer_arr, temp[1])

print(answer)
