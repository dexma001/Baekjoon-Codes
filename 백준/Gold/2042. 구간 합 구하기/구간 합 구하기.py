# 2042

import sys
import math
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list()
arr.append(0)

for i in range(n):
    arr.append(int(input()))

tree = [0] * 2**(math.ceil(math.log(n, 2)) + 1)


def segment(left, right, i=1):
    if left == right:
        tree[i] = arr[left]
        return tree[i]

    mid = (left + right) // 2
    tree[i] = segment(left, mid, i*2) + segment(mid+1, right,
                                                (i*2)+1)
    return tree[i]


segment(1, n, i=1)


def segment_sum(start, end, left, right, i=1):
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return tree[i]

    mid = (start + end) // 2
    return segment_sum(start, mid, left, right, i*2) + segment_sum(mid+1, end, left, right, i*2+1)


def segment_change(start, end, idx, diff, i=1):
    if start > idx or idx > end or diff == 0:
        return -1

    arr[idx] = c
    tree[i] += diff
    if start != end:
        mid = (start+end)//2
        segment_change(start, mid, idx, diff, i*2)
        segment_change(mid+1, end, idx, diff, i*2+1)


for j in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_change(1, n, b, c - arr[b], i=1)
    else:
        print(segment_sum(1, n, b, c, i=1))
