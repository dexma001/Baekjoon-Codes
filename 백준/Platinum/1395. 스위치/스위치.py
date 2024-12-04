# 1395

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seg = list(0 for _ in range(4*n + 1))
lazy_seg = list(0 for _ in range(4*n + 1))


def lazy_update(idx, start, end):
    if lazy_seg[idx]:
        seg[idx] = (end-start+1) - seg[idx]

        if start != end:
            lazy_seg[idx*2] ^= 1
            lazy_seg[idx*2+1] ^= 1

        lazy_seg[idx] = 0


def update_seg(idx, left, right, start, end):
    lazy_update(idx, left, right)

    if end < left or start > right:
        return

    if start <= left and right <= end:
        seg[idx] = (right-left+1) - seg[idx]
        if left != right:
            lazy_seg[idx*2] ^= 1
            lazy_seg[idx*2+1] ^= 1
        return

    mid = (left+right)//2
    update_seg(idx*2, left, mid, start, end)
    update_seg(idx*2+1, mid+1, right, start, end)
    seg[idx] = seg[idx*2] + seg[idx*2+1]


def find_seg(idx, left, right, start, end):
    lazy_update(idx, left, right)
    if start > right or end < left:
        return 0

    if start <= left and right <= end:
        return seg[idx]

    mid = (left+right)//2
    return find_seg(idx*2, left, mid, start, end) + find_seg(idx*2+1, mid+1, right, start, end)


for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        update_seg(1, 1, n, b, c)
    else:
        print(find_seg(1, 1, n, b, c))
