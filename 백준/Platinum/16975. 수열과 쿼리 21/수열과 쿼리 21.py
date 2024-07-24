# 16975

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

level = math.ceil(math.log(n, 2))+1
size = 1 << level
seg_tree = list(0 for _ in range(size+1))


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

seg_lazy = list(0 for _ in range(size+1))


def lazy_update(idx, start, end):
    if seg_lazy[idx] != 0:
        seg_tree[idx] += (end-start+1)*seg_lazy[idx]

        if start != end:
            seg_lazy[idx*2] += seg_lazy[idx]
            seg_lazy[idx*2+1] += seg_lazy[idx]
        seg_lazy[idx] = 0


def seg_update(idx, start, end, left, right, val):
    lazy_update(idx, start, end)

    if left > end or right < start:
        return

    if left <= start and end <= right:
        seg_tree[idx] += (end-start+1)*val
        if start != end:
            seg_lazy[idx*2] += val
            seg_lazy[idx*2+1] += val
        return

    mid = (start+end)//2
    seg_update(idx*2, start, mid, left, right, val)
    seg_update(idx*2+1, mid+1, end, left, right, val)
    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]


def find_seg(idx, start, end, index):
    lazy_update(idx, start, end)

    if index < start or index > end:
        return 0

    if start == index and index == end:
        return seg_tree[idx]

    mid = (start+end)//2

    if start <= index and index <= mid:
        return find_seg(idx*2, start, mid, index)
    else:
        return find_seg(idx*2+1, mid+1, end, index)


for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        seg_update(1, 1, n, temp[1], temp[2], temp[3])
    else:
        print(find_seg(1, 1, n, temp[1]))
