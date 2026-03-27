#9440

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    arr_len = arr.pop(0)
    arr.sort()
    t = arr.count(0)

    arr = arr[t:t+2] +  arr[:t] + arr[t+2:]

    temp = ['', '']
    cnt = 0

    for i in arr:
        temp[cnt] += str(i)
        cnt += 1
        cnt %= 2

    print(int(temp[0]) + int(temp[1]))