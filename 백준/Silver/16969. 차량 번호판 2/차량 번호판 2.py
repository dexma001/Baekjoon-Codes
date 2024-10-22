# 16969

import sys
input = sys.stdin.readline

arr = str(input().strip())
larr = len(arr)

ans = 1
if arr[0] == 'c':
    ans *= 26
else:
    ans *= 10

for i in range(1, len(arr)):
    if arr[i] == 'c':
        if arr[i-1] == 'c':
            ans *= 25
        else:
            ans *= 26
    else:
        if arr[i-1] == 'd':
            ans *= 9
        else:
            ans *= 10
    ans %= 1000000009

print(ans)
