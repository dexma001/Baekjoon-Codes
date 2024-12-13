# 1321

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

seg = list(0 for _ in range(4*n))


def make_seg(idx, start, end):
    if start == end:
        seg[idx] = arr[start]
        return seg[idx]

    mid = (start+end)//2
    make_seg(idx*2, start, mid)
    make_seg(idx*2+1, mid+1, end)
    seg[idx] = seg[idx*2] + seg[idx*2+1]
    return seg[idx]


make_seg(1, 1, n)


def update_seg(idx, start, end, index, value):
    if start > index or end < index:
        return

    if start == end:
        seg[idx] += value
        return seg[idx]

    mid = (start+end)//2
    if index <= mid:
        update_seg(idx*2, start, mid, index, value)
    else:
        update_seg(idx*2+1, mid+1, end, index, value)
    seg[idx] = seg[idx*2] + seg[idx*2+1]
    return seg[idx]


def find_seg(idx, start, end, left, right):
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    return find_seg(idx*2, start, mid, left, right) + find_seg(idx*2+1, mid+1, end, left, right)


def ans(l, r, x):
    while l < r:
        m = (l+r)//2
        if find_seg(1, 1, n, 1, m) < x:
            l = m + 1
        else:
            r = m
    return r


m = int(input())
for _ in range(m):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        update_seg(1, 1, n, arr[1], arr[2])
    else:
        print(ans(1, n, arr[1]))
