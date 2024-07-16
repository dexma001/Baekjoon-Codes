# 2268

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(0 for _ in range(n+1))

height = math.ceil(math.log2(n))+1
node_num = 1 << height
segment_tree = list(0 for _ in range(node_num+1))


def find_segment(idx, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return segment_tree[idx]

    mid = (start+end)//2
    left1 = find_segment(idx*2, start, mid, left, right)
    right1 = find_segment(idx*2+1, mid+1, end, left, right)

    return (left1+right1)


def update_segment(idx, start, end, index, val):
    if start == end:
        segment_tree[idx] = val
        return

    mid = (start+end)//2
    if start <= index and index <= mid:
        update_segment(idx*2, start, mid, index, val)
    else:
        update_segment(idx*2+1, mid+1, end, index, val)

    segment_tree[idx] = (segment_tree[idx*2] + segment_tree[idx*2+1])
    return


for _ in range(m):
    a, p, q = map(int, input().split())
    if a == 0:
        if p > q:
            p, q = q, p
        arr[p] = q
        print(find_segment(1, 1, n, p, q))
    else:
        update_segment(1, 1, n, p, q)
