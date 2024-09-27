# 2437

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if arr[0] != 1:
    print(1)
    quit()

temp = [0, 1]

for i in range(1, n):
    a, b = temp[0]+arr[i], temp[1]+arr[i]
    if a > temp[1]+1:
        print(temp[1]+1)
        break
    else:
        temp = [0, temp[1]+arr[i]]

else:
    print(temp[-1]+1)
