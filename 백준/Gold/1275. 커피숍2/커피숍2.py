# 1275

import math
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

height = math.ceil(math.log2(n))+1
size = 1 << height
seg_tree = list(0 for _ in range(size+1))


def make_seg(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = make_seg(idx*2, left, mid)
    r1 = make_seg(idx*2+1, mid+1, right)

    seg_tree[idx] = l1+r1
    return seg_tree[idx]


make_seg(1, 1, n)


def find_seg(idx, left, right, start, end):
    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = find_seg(idx*2, left, mid, start, end)
    r1 = find_seg(idx*2+1, mid+1, right, start, end)
    return (l1+r1)


def update_seg(idx, left, right, index, val):
    if left == right:
        seg_tree[idx] = val
        return

    mid = (left+right)//2
    if left <= index <= mid:
        update_seg(idx*2, left, mid, index, val)
    else:
        update_seg(idx*2+1, mid+1, right, index, val)

    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]
    return


for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(find_seg(1, 1, n, x, y))
    arr[a] = b
    update_seg(1, 1, n, a, b)
