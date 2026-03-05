#1334

import sys
input = sys.stdin.readline

n = int(input())
arr = str(n+1)
arr_len = len(arr)

if arr_len%2 == 0:
    temp = int(arr[:arr_len//2])
    while True:
        if int(str(temp) + str(temp)[::-1]) >= int(arr):
            break
        temp += 1
    print(str(temp) + str(temp)[::-1])
else:
    temp = int(arr[:arr_len//2+1])
    if int(str(temp) + str(temp)[::-1][1:]) >= int(arr):
        print(str(temp) + str(temp)[::-1][1:])
    else:
        temp += 1
        print(str(temp) + str(temp)[::-1][1:])

