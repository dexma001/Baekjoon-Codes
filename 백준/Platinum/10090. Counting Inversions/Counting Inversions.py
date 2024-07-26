# 10090 - merge sort

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**31-1)

n = int(input())
answer = 0
arr1 = list(map(int, input().split()))


def merge(left, right):
    global answer
    ll, lr = len(left), len(right)
    i, j = 0, 0
    temp = list()
    while i < ll and j < lr:
        if left[i] > right[j]:
            temp.append(right[j])
            j += 1
            answer += ll-i
        else:
            temp.append(left[i])
            i += 1
    if i == ll:
        temp.extend(right[j:])
    else:
        temp.extend(left[i:])
    return temp


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


merge_sort(arr1)
print(answer)
