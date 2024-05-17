# 2565

import sys


def binary_search(i, arr, start, end):
    if start > end:
        return start
    mid = (start+end)//2
    if arr[mid] == i:
        return mid
    elif arr[mid] > i:
        end = mid-1
    else:
        start = mid + 1

    return binary_search(i, arr, start, end)


input = sys.stdin.readline

n = int(input())

arr = dict()
for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b

arr_sort = sorted(arr.items())
arr_end = list(i[1] for i in arr_sort)

dp = list()
lis = list([arr_end[0]])

for i in arr_end[1:]:
    if i > lis[-1]:
        lis.append(i)
    else:
        temp = binary_search(i, lis, 0, len(lis)-1)
        lis[temp] = i


print(n-len(lis))
