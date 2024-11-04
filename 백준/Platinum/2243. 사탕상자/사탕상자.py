# 14268

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = list(0 for _ in range(1000001))

depth = math.ceil(math.log2(1000000))+1
size = 1 << depth
seg_tree = list(0 for _ in range(size+1))


def find_seg(idx, left, right, val):
    seg_tree[idx] -= 1
    if left == right:
        return left
    mid = (left+right)//2
    if seg_tree[idx*2] >= val:
        return find_seg(idx*2, left, mid, val)
    else:
        return find_seg(idx*2+1, mid+1, right, val - seg_tree[idx*2])


def update_seg(idx, left, right, index, value):
    seg_tree[idx] += value
    if left == right:
        return

    mid = (left + right)//2
    if left <= index <= mid:
        update_seg(idx*2, left, mid, index, value)
    else:
        update_seg(idx*2+1, mid+1, right, index, value)


for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        print(find_seg(1, 1, 1000000, temp[1]))
    else:
        update_seg(1, 1, 1000000, temp[1], temp[2])
