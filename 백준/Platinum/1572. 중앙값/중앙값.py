# 1572

import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))

seg_tree = list(0 for _ in range(4*65537+1))


def make_seg(index, start, end, value, diff):
    if start == end:
        seg_tree[index] += diff
        return seg_tree[index]

    mid = (start+end)//2
    if value <= mid:
        make_seg(index*2, start, mid, value, diff)
    else:
        make_seg(index*2+1, mid+1, end, value, diff)
    seg_tree[index] = seg_tree[index*2] + seg_tree[index*2+1]


def find_seg(index, start, end, value):
    if start == end:
        return start

    mid = (start+end)//2
    if value <= seg_tree[index*2]:
        return find_seg(index*2, start, mid, value)
    else:
        return find_seg(index*2+1, mid+1, end, value - seg_tree[index*2])


answer = 0
temp = 0

for i in range(k-1):
    make_seg(1, 0, 65536, arr[i], 1)
for i in range(k-1, n):
    make_seg(1, 0, 65536, arr[i], 1)
    answer += find_seg(1, 0, 65536, (k+1)//2)
    make_seg(1, 0, 65536, arr[temp], -1)
    temp += 1

print(answer)
