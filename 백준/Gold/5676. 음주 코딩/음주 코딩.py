# 5676

import math
import sys
input = sys.stdin.readline


def make_seg(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = make_seg(idx*2, left, mid)
    r1 = make_seg(idx*2+1, mid+1, right)

    seg_tree[idx] = l1*r1
    return seg_tree[idx]


def find_seg(idx, left, right, start, end):
    if start > right or end < left:
        return 1

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left+right)//2
    l1 = find_seg(idx*2, left, mid, start, end)
    r1 = find_seg(idx*2+1, mid+1, right, start, end)
    return (l1*r1)


def update_seg(idx, left, right, index, val):
    if left == right:
        seg_tree[idx] = val
        return

    mid = (left+right)//2
    if left <= index and index <= mid:
        update_seg(idx*2, left, mid, index, val)
    else:
        update_seg(idx*2+1, mid+1, right, index, val)

    seg_tree[idx] = seg_tree[idx*2] * seg_tree[idx*2+1]
    return


while True:
    try:
        a, b = map(int, input().split())
    except:
        break

    arr = [0] + list(map(int, input().split()))
    for i in range(1, a+1):
        if arr[i] > 0:
            arr[i] = 1
        elif arr[i] < 0:
            arr[i] = -1
        else:
            arr[i] = 0

    dep = math.ceil(math.log2(a))+1
    seg_len = 1 << dep
    seg_tree = list(0 for _ in range(seg_len+1))

    make_seg(1, 1, a)

    answer_arr = list()
    for _ in range(b):
        r, p, q = map(str, input().split())
        p = int(p)
        q = int(q)

        if r == 'C':
            if q > 0:
                q = 1
            elif q < 0:
                q = -1
            else:
                q = 0
            arr[p] = q
            update_seg(1, 1, a, p, q)
        else:
            temp = find_seg(1, 1, a, p, q)
            if temp > 0:
                answer_arr.append('+')
            elif temp < 0:
                answer_arr.append('-')
            else:
                answer_arr.append('0')

    print(''.join(answer_arr))
