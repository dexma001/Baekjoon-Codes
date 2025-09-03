# 2374

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque([])
answer = 0

for _ in range(n):
    temp = int(input())
    if not arr:
        arr.append(temp)
    else:
        if temp < arr[-1]:
            arr.append(temp)
        elif temp == arr[-1]:
            continue
        else:
            temp_list = list()
            while arr and arr[-1] < temp:
                temp_list.append(arr.pop())
            answer += (temp - min(temp_list))
            arr.append(temp)

answer += (arr[0] - arr[-1])
print(answer)
