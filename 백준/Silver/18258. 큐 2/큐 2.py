# 18258

from collections import deque
import sys
input = sys.stdin.readline

arr = deque([])
len_arr = 0

for _ in range(int(input())):
    temp = list(map(str, input().split()))
    a = temp[0]
    if len(temp) == 2:
        b = int(temp[1])

    if a == 'push':
        arr.append(b)
        len_arr += 1
    elif a == 'pop':
        if arr:
            print(arr.popleft())
            len_arr -= 1
        else:
            print(-1)
    elif a == 'size':
        print(len_arr)
    elif a == 'empty':
        print(0) if len_arr != 0 else print(1)
    elif a == 'front':
        print(arr[0])if len_arr != 0 else print(-1)
    else:
        print(arr[-1]) if len_arr else print(-1)
