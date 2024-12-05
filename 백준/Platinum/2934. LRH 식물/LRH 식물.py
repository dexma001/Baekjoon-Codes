# 2934

import sys
input = sys.stdin.readline

n = int(input())

seg = list(0 for _ in range(4*100000+1))
lazy = list(0 for _ in range(4*100000+1))


def lazy_update(idx, left, right):
    if lazy[idx] != 0:
        seg[idx] += (right-left+1)*lazy[idx]
        if left != right:
            lazy[idx*2] += lazy[idx]
            lazy[idx*2+1] += lazy[idx]
        lazy[idx] = 0


def update_seg(idx, left, right, start, end, val):
    lazy_update(idx, left, right)

    if left > end or right < start:
        return

    if start <= left and right <= end:
        seg[idx] += (right-left+1) * val
        if left != right:
            lazy[idx*2] += val
            lazy[idx*2+1] += val
        return

    mid = (left+right)//2
    update_seg(idx*2, left, mid, start, end, val)
    update_seg(idx*2+1, mid+1, right, start, end, val)
    seg[idx] = seg[idx*2] + seg[idx*2+1]


def find_seg(idx, left, right, st_end):
    lazy_update(idx, left, right)
    if left > st_end or right < st_end:
        return 0

    if st_end <= left and right <= st_end:
        return seg[idx]

    mid = (left+right)//2
    if st_end <= mid:
        return find_seg(idx*2, left, mid, st_end)
    else:
        return find_seg(idx*2+1, mid+1, right, st_end)


for _ in range(n):
    a, b = map(int, input().split())
    update_seg(1, 1, 100000, a+1, b-1, 1)
    p = find_seg(1, 1, 100000, a)
    q = find_seg(1, 1, 100000, b)

    print(p+q)

    if p != 0:
        update_seg(1, 1, 100000, a, a, -p)
    if q != 0:
        update_seg(1, 1, 100000, b, b, -q)
