# 18185

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) + [0, 0]
price = 0

for i in range(n):
    if arr[i]:
        if arr[i+1] > arr[i+2]:
            cnt = min(arr[i], arr[i+1]-arr[i+2])
            price += 5*cnt
            arr[i] -= cnt
            arr[i+1] -= cnt

            cnt2 = min(arr[i], arr[i+1], arr[i+2])
            price += 7*cnt2
            arr[i] -= cnt2
            arr[i+1] -= cnt2
            arr[i+2] -= cnt2

        else:
            cnt2 = min(arr[i], arr[i+1])
            price += 7*cnt2
            arr[i] -= cnt2
            arr[i+1] -= cnt2
            arr[i+2] -= cnt2

            cnt = min(arr[i], arr[i+1])
            price += 5*cnt
            arr[i] -= cnt
            arr[i+1] -= cnt

        price += 3*arr[i]

print(price)
