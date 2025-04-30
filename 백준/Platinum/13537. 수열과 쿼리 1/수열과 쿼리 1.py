# 13537

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

seg = list([] for _ in range(4*n))

def merge(left, right, a, b):
    i, j = 0, 0
    sorted_list = list()

    while i < a and j < b:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def make_seg(start, end, idx):
    if start == end:
        seg[idx].append(arr[start])
        return seg[idx]

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = merge(seg[idx*2], seg[idx*2+1],
                     len(seg[idx*2]), len(seg[idx*2+1]))

make_seg(1, n, 1)

def binary_search(start, end, arr, val):
    if start == end:
        return start
    mid = (start+end)//2
    if arr[mid] > val:
        return binary_search(start, mid, arr, val)
    else:
        return binary_search(mid+1, end, arr, val)

def find_seg(start, end, left, right, idx, k, value):
    if right < start or end < left:
        return value

    if left <= start and end <= right:
        p = binary_search(0, len(seg[idx])-1, seg[idx], k)
        if seg[idx][p] > k:
            return (len(seg[idx])-p)
        else:
            return (len(seg[idx])-p-1)

    mid = (start + end) // 2
    a = 0
    b = 0
    if seg[idx*2][-1] > k:
        a = find_seg(start, mid, left, right, idx*2, k, 0)
    if seg[idx*2+1][-1] > k:
        b = find_seg(mid+1, end, left, right, idx*2+1, k, 0)
    return (a+b)


for _ in range(int(input())):
    i, j, k = map(int, input().split())
    print(find_seg(1, n, i, j, 1, k, 0))
