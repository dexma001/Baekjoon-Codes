# 18436

import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

depth = math.ceil(math.log2(n))+1
size = 1 << depth

odd_seg_tree = list(0 for _ in range(size+1))


def make_odd_seg(idx, start, end):
    if start == end:
        if (arr[start] % 2) != 0:
            odd_seg_tree[idx] += 1
        return odd_seg_tree[idx]

    mid = (start+end)//2
    l1 = make_odd_seg(idx*2, start, mid)
    r1 = make_odd_seg(idx*2+1, mid+1, end)
    odd_seg_tree[idx] = l1+r1
    return odd_seg_tree[idx]


make_odd_seg(1, 1, n)


def update_odd_seg(idx, start, end, index, value):
    if start == end:
        if arr[start] % 2 != 0:
            odd_seg_tree[idx] += 1
        else:
            odd_seg_tree[idx] -= 1
        return

    mid = (start+end)//2
    if start <= index and index <= mid:
        update_odd_seg(idx*2, start, mid, index, value)
    else:
        update_odd_seg(idx*2+1, mid+1, end, index, value)
    odd_seg_tree[idx] = odd_seg_tree[idx*2] + odd_seg_tree[idx*2+1]
    return


def find_seg(idx, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return odd_seg_tree[idx]

    mid = (start+end)//2
    l1 = find_seg(idx*2, start, mid, left, right)
    r1 = find_seg(idx*2+1, mid+1, end, left, right)
    return l1 + r1


for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        if temp[2] % 2 != arr[temp[1]] % 2:
            arr[temp[1]] = temp[2]
            update_odd_seg(1, 1, n, temp[1], temp[2])
    elif temp[0] == 2:
        print((temp[2]-temp[1]+1)-find_seg(1, 1, n, temp[1], temp[2]))
    else:
        print(find_seg(1, 1, n, temp[1], temp[2]))
