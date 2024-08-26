# 13913

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer_arr = list()

if n >= m:
    print(n-m)
    answer_arr = list(i for i in range(n, m-1, -1))
    print(*answer_arr)

else:
    arr = list(0 for _ in range(100001))
    stack = deque([])
    stack.append([n, [n]])

    while stack:
        temp, temp_arr = stack.popleft()
        if temp == m:
            print(arr[temp])
            print(*temp_arr)
            break

        for i in (temp-1, temp+1, temp*2):
            if 0 <= i <= 100000 and not arr[i]:
                arr[i] = arr[temp] + 1
                stack.append([i, temp_arr+[i]])
