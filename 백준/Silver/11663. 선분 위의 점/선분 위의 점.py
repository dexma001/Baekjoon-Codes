# 11663

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def binary_search(st, end, value):
    if st == end:
        return st

    mid = (st+end)//2

    if arr[mid] == value:
        return mid

    elif value > arr[mid]:
        st = mid+1
    else:
        end = mid
    return binary_search(st, end, value)


for _ in range(m):
    left, right = map(int, input().split())
    if left > right:
        left, right = right, left

    if left > arr[-1] or right < arr[0]:
        print(0)
        continue

    start = binary_search(0, n-1, left)
    end_1 = binary_search(start, n-1, right)

    temp = (end_1 - start+1)

    if arr[end_1] > right:
        temp -= 1

    print(temp)
