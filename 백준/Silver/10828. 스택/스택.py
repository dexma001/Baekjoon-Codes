# 10828

from collections import deque
import sys
input = sys.stdin.readline

arr = deque([])

for _ in range(int(input())):
    temp = list(map(str, input().split()))
    a = temp[0]
    if len(temp) == 2:
        b = int(temp[1])

    if a == "push":
        arr.appendleft(b)
    elif a == "pop":
        print(arr.popleft()) if len(arr) > 0 else print(-1)
    elif a == "size":
        print(len(arr))
    elif a == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        print(arr[0]) if len(arr) > 0 else print(-1)
