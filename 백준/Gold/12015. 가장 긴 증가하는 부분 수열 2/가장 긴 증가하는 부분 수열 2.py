# 12015

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans_arr = list([arr[0]])


def binary_search(start, end, target):
    if start > end:
        return start

    mid = (start + end)//2

    if ans_arr[mid] > target:
        return binary_search(start, mid-1, target)
    elif ans_arr[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return mid


for i in range(1, n):
    if arr[i] > ans_arr[-1]:
        ans_arr.append(arr[i])
    else:
        loc = binary_search(0, len(ans_arr)-1, arr[i])
        ans_arr[loc] = arr[i]

print(len(ans_arr))
