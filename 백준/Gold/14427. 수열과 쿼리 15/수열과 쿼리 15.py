# 14427

import heapq
from collections import defaultdict
import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
index_value = defaultdict(list)
for i in range(1, n+1):
    heapq.heappush(index_value[arr[i]], i)

level = math.ceil(math.log2(n))+1
seg_len = 1 << level
seg_tree = list(0 for _ in range(seg_len+1))


def make_seg(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = make_seg(idx*2, left, mid)
    r1 = make_seg(idx*2+1, mid+1, right)
    seg_tree[idx] = min(l1, r1)
    return seg_tree[idx]


make_seg(1, 1, n)


def update_seg(idx, left, right, index, value):
    if left == right:
        index_value[seg_tree[idx]].remove(left)
        heapq.heapify(index_value[seg_tree[idx]])
        seg_tree[idx] = value
        heapq.heappush(index_value[value], index)
        return
    mid = (left+right)//2
    if left <= index and index <= mid:
        update_seg(idx*2, left, mid, index, value)
    else:
        update_seg(idx*2+1, mid+1, right, index, value)
    seg_tree[idx] = min(seg_tree[idx*2], seg_tree[idx*2+1])
    return


for _ in range(int(input())):
    temp_arr = list(map(int, input().split()))
    if temp_arr[0] == 1:
        arr[temp_arr[1]] = temp_arr[2]
        update_seg(1, 1, n, temp_arr[1], temp_arr[2])
    else:
        print(index_value[seg_tree[1]][0])
