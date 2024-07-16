# 14438

import math
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = 10**9

n = int(input())
arr = [0] + list(map(int, input().split()))

height = math.ceil(math.log2(n)) + 1
node_num = 1 << height
segment_tree = [0] + list(0 for _ in range(node_num))


def make_segment(idx, start, end):
    if start == end:
        segment_tree[idx] = arr[start]
        return segment_tree[idx]

    mid = (start+end)//2

    left = make_segment(idx*2, start, mid)
    right = make_segment(idx*2+1, mid+1, end)

    segment_tree[idx] = min(left, right)

    return segment_tree[idx]


make_segment(1, 1, n)


def find_segment(idx, start, end, left, right):
    if right < start or left > end:
        return 10**9+10

    if left <= start and end <= right:
        return segment_tree[idx]

    mid = (start+end)//2
    left1 = find_segment(idx*2, start, mid, left, right)
    right1 = find_segment(idx*2+1, mid+1, end, left, right)
    return min(left1, right1)


def update(idx, start, end, index, val):
    if start == end:
        segment_tree[idx] = val
        return

    mid = (start+end)//2
    if start <= index and index <= mid:
        update(idx*2, start, mid, index, val)
    else:
        update(idx*2+1, mid+1, end, index, val)
    segment_tree[idx] = min(segment_tree[idx*2], segment_tree[idx*2+1])
    return


for _ in range(int(input())):
    a, p, q = map(int, input().split())
    if a == 1:
        arr[p] = q
        update(1, 1, n, p, q)
    else:
        print(find_segment(1, 1, n, p, q))
