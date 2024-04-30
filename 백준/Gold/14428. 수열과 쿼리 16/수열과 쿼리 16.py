# 14428

import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
arr = [0] + list(map(int, input().split()))

size = math.ceil(math.log(n, 2) + 1)
segment_tree = list(10**10 for _ in range(2**size))
size -= 1


def segment_setting(left, right, i):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]
    mid = (left + right) // 2
    segment_tree[i] = min(segment_setting(left, mid, i*2),
                          segment_setting(mid+1, right, i*2+1))
    return segment_tree[i]


segment_setting(1, n, 1)


def segment_update(start, end, idx, diff, i):
    if start > idx or idx > end:
        return segment_tree[i]
    if start == end:
        if start == idx:
            segment_tree[i] = diff
        return segment_tree[i]
    mid = (start + end) // 2
    if idx <= mid:
        segment_tree[i] = min(segment_tree[i*2+1],
                              segment_update(start, mid, idx, diff, i*2))
    else:
        segment_tree[i] = min(
            segment_tree[i*2], segment_update(mid+1, end, idx, diff, i*2+1))
    return segment_tree[i]


def segment_search(left, right, nodeleft, noderight, i):
    if right < nodeleft or left > noderight:
        return 10**10
    if left <= nodeleft and noderight <= right:
        return segment_tree[i]

    mid = (nodeleft + noderight) // 2
    return min(segment_search(left, right, nodeleft, mid, i*2), segment_search(left, right, mid+1, noderight, i*2+1))


for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x == 1:
        arr[y] = z
        segment_update(1, n, y, z, 1)
    else:
        a = (segment_search(y, z, 1, n, 1))
        for i in range(y, z+1):
            if arr[i] == a:
                print(i)
                break
