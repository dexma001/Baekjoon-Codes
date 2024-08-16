# 9426

import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
maxn = 65535
arr = list(int(input()) for _ in range(n))

seg_tree = list(0 for _ in range(4*65537))


def make_seg(idx, start, end, value, diff):
    if start == end:
        seg_tree[idx] += diff
        return seg_tree[idx]

    mid = (start+end)//2
    if value <= mid:
        make_seg(idx*2, start, mid, value, diff)
    else:
        make_seg(idx*2+1, mid+1, end, value, diff)

    seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]
    return seg_tree[idx]


def find_seg(idx, start, end, value):
    if start == end:
        return start

    mid = (start+end)//2
    if value <= seg_tree[idx*2]:
        return find_seg(idx*2, start, mid, value)
    else:
        return find_seg(idx*2+1, mid+1, end, value-seg_tree[idx*2])


answer = 0
temp = 0

for i in range(k-1):
    make_seg(1, 0, maxn, arr[i], 1)

for i in range(k-1, n):
    make_seg(1, 0, maxn, arr[i], 1)
    answer += find_seg(1, 0, maxn, math.floor((k+1)/2))
    make_seg(1, 0, maxn, arr[temp], -1)
    temp += 1

print(answer)
