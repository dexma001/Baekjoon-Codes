# 28279

from collections import deque
import sys
input = sys.stdin.readline

arr = deque([])

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        arr.appendleft(temp[1])
    elif temp[0] == 2:
        arr.append(temp[1])
    elif temp[0] == 3:
        print(arr.popleft()) if arr else print(-1)
    elif temp[0] == 4:
        print(arr.pop()) if arr else print(-1)
    elif temp[0] == 5:
        print(len(arr))
    elif temp[0] == 6:
        print(1) if not arr else print(0)
    elif temp[0] == 7:
        if arr:
            k = arr.popleft()
            print(k)
            arr.appendleft(k)
        else:
            print(-1)
    elif temp[0] == 8:
        if arr:
            t = arr.pop()
            print(t)
            arr.append(t)
        else:
            print(-1)
