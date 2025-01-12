# 15787

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(0 for _ in range(n+1))

for _ in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:

        arr[temp[1]] |= (1 << temp[2]-1)
    elif temp[0] == 2:

        arr[temp[1]] &= ~(1 << temp[2]-1)
    elif temp[0] == 3:
        arr[temp[1]] <<= 1
        arr[temp[1]] &= ~(1 << 20)
    else:
        arr[temp[1]] >>= 1

arr.pop(0)
print(len(set(arr)))
