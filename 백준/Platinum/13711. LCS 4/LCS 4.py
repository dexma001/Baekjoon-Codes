# 13711

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

temp = dict()

for i in range(n):
    temp[arr1[i]] = i

r_arr = list()

for i in arr2:
    r_arr.append(temp[i])


def binary_search(start, end, arr, target):
    if start > end:
        return start

    mid = (start+end)//2
    if target < arr[mid]:
        return binary_search(start, mid-1, arr, target)
    elif target == arr[mid]:
        return mid
    else:
        return binary_search(mid+1, end, arr, target)


lis = [r_arr[0]]

for i in range(1, n):
    if r_arr[i] > lis[-1]:
        lis.append(r_arr[i])

    else:
        idx = binary_search(0, len(lis)-1, lis, r_arr[i])
        lis[idx] = r_arr[i]

print(len(lis))
