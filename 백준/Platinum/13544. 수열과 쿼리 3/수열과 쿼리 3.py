# 13544

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

seg = list([] for _ in range(4*n))


def merge_sort(left, right, left_len, right_len):
    i = 0
    j = 0
    temp = list()
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    temp += left[i:]
    temp += right[j:]
    return temp


def make_seg(start, end, idx):
    if start == end:
        seg[idx].append(arr[start])
        return seg[idx]

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = merge_sort(seg[idx*2], seg[idx*2+1],
                          len(seg[idx*2]), len(seg[idx*2+1]))
    return seg[idx]


make_seg(1, n, 1)


def binary_search(start, end, arr, value):
    if start == end:
        return start

    mid = (start+end)//2
    if arr[mid] > value:
        return binary_search(start, mid, arr, value)
    else:
        return binary_search(mid+1, end, arr, value)


def find_seg(start, end, left, right, idx, k, value):
    if right < start or end < left:
        return value

    if left <= start and end <= right:
        t = binary_search(0, len(seg[idx])-1, seg[idx], k)
        if seg[idx][t] <= k:
            return (len(seg[idx]) - t - 1)
        else:
            return (len(seg[idx]) - t)

    mid = (start+end)//2
    l = 0
    r = 0
    if seg[idx*2][-1] > k:
        l = find_seg(start, mid, left, right, idx*2, k, 0)
    if seg[idx*2+1][-1] > k:
        r = find_seg(mid+1, end, left, right, idx*2+1, k, 0)
    return (l+r)


answer = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    i = (answer ^ a)
    j = (answer ^ b)
    k = (answer ^ c)
    answer = find_seg(1, n, i, j, 1, k, 0)
    print(answer)
