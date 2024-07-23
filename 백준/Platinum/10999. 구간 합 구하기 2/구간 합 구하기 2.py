# 10999

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] + list(int(input()) for _ in range(n))

size = math.ceil(math.log2(n)) + 1
size_ = 1 << size
seg = list(0 for _ in range(size_+1))
lazy_seg = list(0 for _ in range(size_+1))


def make_seg(idx, left, right):
    if left == right:
        seg[idx] = arr[left]
        return seg[idx]

    mid = (left+right)//2
    l1 = make_seg(idx*2, left, mid)
    r1 = make_seg(idx*2+1, mid+1, right)
    seg[idx] = l1+r1
    return seg[idx]


make_seg(1, 1, n)


def lazy_update(idx, start, end):
    if lazy_seg[idx] != 0:
        seg[idx] += (end-start+1)*lazy_seg[idx]

        if start != end:
            lazy_seg[idx*2] += lazy_seg[idx]
            lazy_seg[idx*2+1] += lazy_seg[idx]

        lazy_seg[idx] = 0


def find_seg(idx, left, right, start, end):
    lazy_update(idx, left, right)

    if start > right or end < left:
        return 0

    if start <= left and right <= end:
        return seg[idx]

    mid = (left+right)//2
    l1 = find_seg(idx*2, left, mid, start, end)
    r1 = find_seg(idx*2+1, mid+1, right, start, end)
    return (l1+r1)


def update_seg(idx, left, right, start, end, val):
    lazy_update(idx, left, right)

    if end < left or right < start:
        return

    if start <= left and right <= end:
        seg[idx] += (right-left+1)*val
        if left != right:
            lazy_seg[idx*2] += val
            lazy_seg[idx*2+1] += val
        return

    mid = (left+right)//2
    update_seg(idx*2, left, mid, start, end, val)
    update_seg(idx*2+1, mid+1, right, start, end, val)
    seg[idx] = seg[idx*2] + seg[idx*2+1]


for _ in range(m+k):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update_seg(1, 1, n, temp[1], temp[2], temp[3])
    else:
        print(find_seg(1, 1, n, temp[1], temp[2]))
