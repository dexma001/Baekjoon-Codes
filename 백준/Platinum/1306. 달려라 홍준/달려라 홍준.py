# 1306

from collections import deque
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

size = math.ceil(math.log2(n)) + 1
size_ = 1 << size
seg_tree = list(0 for _ in range(size_+1))


def make_seg(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = make_seg(idx*2, left, mid)
    r1 = make_seg(idx*2+1, mid+1, right)
    seg_tree[idx] = max(l1, r1)
    return seg_tree[idx]


make_seg(1, 1, n)


def find_seg(idx, left, right, start, end):
    if left > end or right < start:
        return 0

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = find_seg(idx*2, left, mid, start, end)
    r1 = find_seg(idx*2+1, mid+1, right, start, end)
    return max(l1, r1)


answer = list()
for i in range(m, n-m+2):
    l1 = i-(m-1)
    r1 = i+(m-1)
    l11 = l1-1
    if not answer or arr[l11] == answer[-1] or arr[r1] > answer[-1]:
        answer.append(find_seg(1, 1, n, l1, r1))
    else:
        answer.append(answer[-1])

print(*answer)
