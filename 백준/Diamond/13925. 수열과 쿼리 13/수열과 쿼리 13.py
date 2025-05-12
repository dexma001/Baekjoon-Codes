# 13925

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
mod = 1000000007

seg = list(0 for _ in range(4*n+1))
lazy_seg = list([1, 0] for _ in range(4*n+1))  # 곱하는거 / 더하는거


def make_seg(start, end, idx):
    if start == end:
        seg[idx] = arr[start]
        return seg[idx]

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = (seg[idx*2] + seg[idx*2+1]) % mod


make_seg(1, n, 1)


def lazy(start, end, idx):
    if lazy_seg[idx] != [1, 0]:
        seg[idx] = (lazy_seg[idx][0] * seg[idx] +
                    (lazy_seg[idx][1]*(end-start+1))) % mod

        if start != end:
            lazy_seg[idx*2][0] *= lazy_seg[idx][0]
            lazy_seg[idx*2][1] = lazy_seg[idx][0] * \
                lazy_seg[idx*2][1] + lazy_seg[idx][1]  # copy
            lazy_seg[idx*2][0] %= mod
            lazy_seg[idx*2][1] %= mod

            lazy_seg[idx*2+1][0] *= lazy_seg[idx][0]
            lazy_seg[idx*2+1][1] = lazy_seg[idx][0] * \
                lazy_seg[idx*2+1][1] + lazy_seg[idx][1]  # copy
            lazy_seg[idx*2+1][0] %= mod
            lazy_seg[idx*2+1][1] %= mod

        lazy_seg[idx] = [1, 0]


def update_seg(start, end, left, right, multi, sum, idx):
    lazy(start, end, idx)

    if left > end or right < start:
        return

    if left <= start and end <= right:  # copy
        lazy_seg[idx][0] *= multi
        lazy_seg[idx][0] %= mod

        lazy_seg[idx][1] *= multi
        lazy_seg[idx][1] %= mod

        lazy_seg[idx][1] += sum
        lazy_seg[idx][1] %= mod

        lazy(start, end, idx)
        return

    mid = (start+end)//2
    update_seg(start, mid, left, right, multi, sum,  idx*2)
    update_seg(mid+1, end, left, right, multi, sum, idx*2+1)
    seg[idx] = (seg[idx*2] + seg[idx*2+1]) % mod


def find_seg(start, end, left, right, idx):
    lazy(start, end, idx)
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    l = find_seg(start, mid, left, right, idx*2)
    r = find_seg(mid+1, end, left, right, idx*2+1)
    return (l+r) % mod


for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 4:
        print(find_seg(1, n, temp[1], temp[2], 1))
    else:
        if temp[0] == 1:
            update_seg(1, n, temp[1], temp[2], 1, temp[3], 1)  # non copy
        elif temp[0] == 2:
            update_seg(1, n, temp[1], temp[2], temp[3], 0, 1)  # non copy
        else:
            update_seg(1, n, temp[1], temp[2], 0, temp[3], 1)  # non copy
