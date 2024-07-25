# 1517

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(0, n+1):
    arr[i] = [i, arr[i]]
arr.sort(key=lambda x: [x[1], x[0]])

depth = math.ceil(math.log2(n))+1
size = 1 << depth
seg_tree = list(0 for _ in range(size+1))


def find_seg(idx, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[idx]

    mid = (start+end)//2
    l1 = find_seg(idx*2, start, mid, left, right)
    r1 = find_seg(idx*2+1, mid+1, end, left, right)
    return (l1+r1)


def update_seg(idx, start, end, index):
    if start == end:
        seg_tree[idx] += 1
        return

    seg_tree[idx] += 1
    mid = (start+end)//2
    if start <= index and index <= mid:
        update_seg(idx*2, start, mid, index)
    else:
        update_seg(idx*2+1, mid+1, end, index)


answer = 0
for i in range(1, n+1):
    answer += find_seg(1, 1, n, arr[i][0], n)
    update_seg(1, 1, n, arr[i][0])

print(answer)
