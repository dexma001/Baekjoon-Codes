# 10811

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(i for i in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    temp_arr = arr[a:b+1]
    temp_arr.reverse()
    for i in range(b-a+1):
        arr[a+i] = temp_arr[i]

print(*arr[1:])
