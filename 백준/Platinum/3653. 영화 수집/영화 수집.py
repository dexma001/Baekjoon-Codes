# 3653

import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [1]*(n+1)+[0]*(m)
    dvd_idx = {n+1-i: i for i in range(1, n+1)}
    want_to_watch = list(map(int, input().split()))

    size = math.ceil(math.log2(n+m)) + 1
    size_ = 1 << size
    seg_tree = list(0 for _ in range(size_+1))

    def make_seg(idx, left, right):
        if left == right:
            seg_tree[idx] = arr[left]
        else:
            mid = (left+right)//2
            make_seg(idx*2, left, mid)
            make_seg(idx*2+1, mid+1, right)
            seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]
        return seg_tree[idx]

    make_seg(1, 1, n+m)

    def find_seg(idx, left, right, start, end):
        if start > right or end < left:
            return 0
        if start <= left and right <= end:
            return seg_tree[idx]

        mid = (left+right)//2
        l1 = find_seg(idx*2, left, mid, start, end)
        r1 = find_seg(idx*2+1, mid+1, right, start, end)
        return l1 + r1

    def update_seg(idx, left, right, new_idx, value):
        if right < new_idx or left > new_idx:
            return

        if left == right:
            seg_tree[idx] = value

        else:
            mid = (left+right)//2
            update_seg(idx*2, left, mid, new_idx, value)
            update_seg(idx*2+1, mid+1, right, new_idx, value)
            seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]
        return seg_tree[idx]

    answer = list()
    new_idx = n
    for i in want_to_watch:
        index = dvd_idx[i]
        answer.append(find_seg(1, 1, n+m, index+1, new_idx))
        update_seg(1, 1, n+m, index, 0)
        new_idx += 1
        update_seg(1, 1, n+m, new_idx, 1)
        dvd_idx[i] = new_idx
    print(*answer)
