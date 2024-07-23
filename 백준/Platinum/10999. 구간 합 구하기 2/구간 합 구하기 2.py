# 10999

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] + list(int(input()) for _ in range(n))

size = math.ceil(math.log2(n))+1
size_ = 1 << size
seg = list(0 for _ in range(size_+1))
lazy_seg = list(0 for _ in range(size_+1))


def make_seg(idx, start, end):
    if start == end:
        seg[idx] = arr[start]
        return seg[idx]

    mid = (start+end)//2
    l1 = make_seg(idx*2, start, mid)
    r1 = make_seg(idx*2+1, mid+1, end)
    seg[idx] = l1+r1
    return seg[idx]


make_seg(1, 1, n)


def update_lazy(idx, start, end):
    if lazy_seg[idx] != 0:
        seg[idx] += (end-start+1)*lazy_seg[idx]

        if start != end:
            lazy_seg[idx*2] += lazy_seg[idx]
            lazy_seg[idx*2+1] += lazy_seg[idx]

        lazy_seg[idx] = 0


def update_seg(idx, start, end, left, right, val):
    update_lazy(idx, start, end)

    if left > end or right < start:
        return

    if left <= start and end <= right:
        seg[idx] += (end-start+1)*val
        if start != end:
            lazy_seg[idx*2] += val
            lazy_seg[idx*2+1] += val
        return

    mid = (start+end)//2
    update_seg(idx*2, start, mid, left, right, val)
    update_seg(idx*2+1, mid+1, end, left, right, val)
    seg[idx] = seg[idx*2]+seg[idx*2+1]


def find_seg(idx, start, end, left, right):
    update_lazy(idx, start, end)

    if right < start or left > end:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    l1 = find_seg(idx*2, start, mid, left, right)
    r1 = find_seg(idx*2+1, mid+1, end, left, right)
    return l1+r1


for _ in range(m+k):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update_seg(1, 1, n, temp[1], temp[2], temp[3])
    else:
        print(find_seg(1, 1, n, temp[1], temp[2]))
