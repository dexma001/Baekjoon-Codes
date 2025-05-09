# 12844

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

seg = list(0 for _ in range(4*n+1))
lazy_seg = list(0 for _ in range(4*n+1))


def make_seg(start, end, idx):
    if start == end:
        seg[idx] = arr[start]
        return seg[idx]

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = seg[idx*2] ^ seg[idx*2+1]
    return seg[idx]


make_seg(1, n, 1)


def lazy_update(start, end, idx):
    if lazy_seg[idx]:
        seg[idx] ^= lazy_seg[idx] * ((end-start+1) % 2)
        if start != end:
            lazy_seg[idx*2] ^= lazy_seg[idx]
            lazy_seg[idx*2+1] ^= lazy_seg[idx]

        lazy_seg[idx] = 0


def update(start, end, left, right, idx, value):
    lazy_update(start, end, idx)

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        seg[idx] ^= value * ((end-start+1) % 2)
        if start != end:
            lazy_seg[idx*2] ^= value
            lazy_seg[idx*2+1] ^= value
        return seg[idx]

    mid = (start+end)//2
    update(start, mid, left, right, idx*2, value)
    update(mid+1, end, left, right, idx*2+1, value)
    seg[idx] = seg[idx*2] ^ seg[idx*2+1]
    return seg[idx]


def find_seg(start, end, left, right, idx):
    lazy_update(start, end, idx)
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    l = find_seg(start, mid, left, right, idx*2)
    r = find_seg(mid+1, end, left, right, idx*2+1)
    return l ^ r


for _ in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update(1, n, temp[1]+1, temp[2]+1, 1, temp[3])
    else:
        print(find_seg(1, n, temp[1]+1, temp[2]+1, 1))
