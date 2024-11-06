# 15967

import math
import sys
input = sys.stdin.readline

n, q1, q2 = map(int, input().split())

arr = [0] + list(map(int, input().split()))
size = math.ceil(math.log2(n)) + 1
size_ = 1 << size

seg_tree = list(0 for _ in range(size_ + 1))
lazy_seg = list(0 for _ in range(size_ + 1))


def make_seg(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left+right)//2
    seg_tree[idx] = make_seg(idx*2, left, mid) + \
        make_seg(idx*2+1, mid+1, right)
    return seg_tree[idx]


make_seg(1, 1, n)


def lazy_update(idx, left, right):
    if lazy_seg[idx] != 0:
        seg_tree[idx] += (right-left+1)*lazy_seg[idx]

        if left != right:
            lazy_seg[idx*2] += lazy_seg[idx]
            lazy_seg[idx*2+1] += lazy_seg[idx]

        lazy_seg[idx] = 0


def seg_find(idx, left, right, start, end):
    lazy_update(idx, left, right)

    if start > right or end < left:
        return 0

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = seg_find(idx*2, left, mid, start, end)
    r1 = seg_find(idx*2+1, mid+1, right, start, end)
    return l1+r1


def seg_update(idx, left, right, start, end, value):
    lazy_update(idx, left, right)

    if end < left or start > right:
        return

    if start <= left and right <= end:
        seg_tree[idx] += (right-left+1)*value
        if left != right:
            lazy_seg[idx*2] += value
            lazy_seg[idx*2+1] += value
        return

    mid = (left+right)//2
    seg_update(idx*2, left, mid, start, end, value)
    seg_update(idx*2+1, mid+1, right, start, end, value)
    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]


for _ in range(q1+q2):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        print(seg_find(1, 1, n, temp[1], temp[2]))
    else:
        seg_update(1, 1, n, temp[1], temp[2], temp[3])
