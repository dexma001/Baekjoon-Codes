# 1655

import heapq
import sys
input = sys.stdin.readline

arr_left = list()
arr_right = list()

for i in range(int(input())):
    temp = int(input())

    if i == 0:
        print(temp)
        heapq.heappush(arr_left, (-temp, temp))
    elif i == 1:
        if temp > arr_left[0][1]:
            print(arr_left[0][1])
            heapq.heappush(arr_right, temp)
        else:
            print(temp)
            a, b = heapq.heappop(arr_left)
            heapq.heappush(arr_left, (-temp, temp))
            heapq.heappush(arr_right, b)

    else:
        if i % 2 == 0:
            if temp > arr_left[0][1]:
                heapq.heappush(arr_right, temp)
                print(arr_right[0])
            else:
                a, b = heapq.heappop(arr_left)
                heapq.heappush(arr_left, (-temp, temp))
                heapq.heappush(arr_right, b)
                print(arr_right[0])
        else:
            if temp > arr_right[0]:
                a = heapq.heappop(arr_right)
                heapq.heappush(arr_right, temp)
                heapq.heappush(arr_left, (-a, a))
                print(arr_left[0][1])
            else:
                heapq.heappush(arr_left, (-temp, temp))
                print(arr_left[0][1])
