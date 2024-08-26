# 1697

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n >= m:
    print(n-m)

else:
    arr = list(0 for _ in range(100001))
    stack = deque([])
    stack.append(n)

    while stack:
        temp = stack.popleft()
        if temp == m:
            print(arr[temp])
            break

        for i in (temp-1, temp+1, temp*2):
            if 0 <= i <= 100000 and not arr[i]:
                arr[i] = arr[temp] + 1
                stack.append(i)
