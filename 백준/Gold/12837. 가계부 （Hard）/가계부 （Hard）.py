# 12837

import math
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(0 for _ in range(n+1))

level = math.ceil(math.log2(n))+1
size = 1 << level
seg_tree = list(0 for _ in range(size+1))


def update_seg(idx, start, end, index, value):
    if start == end:
        seg_tree[idx] += value
        return

    mid = (start+end)//2
    if start <= index and index <= mid:
        update_seg(idx*2, start, mid, index, value)
    else:
        update_seg(idx*2+1, mid+1, end, index, value)
    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]
    return


def find_seg(idx, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return seg_tree[idx]

    mid = (start+end)//2
    l1 = find_seg(idx*2, start, mid, left, right)
    r1 = find_seg(idx*2+1, mid+1, end, left, right)
    return (l1+r1)


for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        arr[temp[1]] += temp[2]
        update_seg(1, 1, n, temp[1], temp[2])
    else:
        print(find_seg(1, 1, n, temp[1], temp[2]))
