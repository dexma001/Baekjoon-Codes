# 2696

import math
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list()
    for _ in range(n//10+1):
        arr.extend(list(map(int, input().split())))

    odd_middle_num = list()

    left_heap = list()
    right_heap = list()

    heapq.heappush(left_heap, arr[0])
    odd_middle_num.append(arr[0])

    for i in range(1, n):
        if i % 2 != 0:
            if arr[i] > left_heap[0]:
                temp = heapq.heappop(left_heap)
                heapq.heappush(left_heap, arr[i])
                heapq.heappush(right_heap, -temp)
            else:
                heapq.heappush(right_heap, -arr[i])
        else:
            if arr[i] > -right_heap[0]:
                heapq.heappush(left_heap, arr[i])
                odd_middle_num.append(left_heap[0])
            else:
                temp = heapq.heappop(right_heap)
                heapq.heappush(right_heap, -arr[i])
                heapq.heappush(left_heap, -temp)
                odd_middle_num.append(left_heap[0])

    print(math.ceil(n/2))
    print(*odd_middle_num)
