# 14245

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

depth = math.ceil(math.log2(n))+1
size = 1 << depth
seg_tree = list(0 for _ in range(size+1))
lazy_seg = list(0 for _ in range(size+1))


def make_seg(idx, start, end):
    if start == end:
        seg_tree[idx] = arr[start]
        return seg_tree[idx]
    mid = (start+end)//2
    l1 = make_seg(idx*2, start, mid)
    r1 = make_seg(idx*2+1, mid+1, end)
    seg_tree[idx] = l1+r1
    return seg_tree[idx]


make_seg(1, 1, n)


def lazy_update(idx, start, end):
    if lazy_seg[idx] != 0:
        seg_tree[idx] ^= lazy_seg[idx]

        if start != end:
            lazy_seg[idx*2] ^= lazy_seg[idx]
            lazy_seg[idx*2+1] ^= lazy_seg[idx]
        lazy_seg[idx] = 0


def find_seg(idx, start, end, index):
    lazy_update(idx, start, end)

    if start == index and index == end:
        return seg_tree[idx]

    mid = (start+end)//2
    if start <= index and index <= mid:
        return find_seg(idx*2, start, mid, index)
    else:
        return find_seg(idx*2+1, mid+1, end, index)


def update_seg(idx, start, end, left, right, value):
    lazy_update(idx, start, end)

    if end < left or right < start:
        return

    if left <= start and end <= right:
        seg_tree[idx] ^= value
        if start != end:
            lazy_seg[idx*2] ^= value
            lazy_seg[idx*2+1] ^= value
        return

    mid = (start+end)//2
    update_seg(idx*2, start, mid, left, right, value)
    update_seg(idx*2+1, mid+1, end, left, right, value)
    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]


for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update_seg(1, 1, n, temp[1]+1, temp[2]+1, temp[3])
    else:
        print(find_seg(1, 1, n, temp[1]+1))
