# 1280

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(int(input()) for _ in range(n))

cnt_seg = list(0 for _ in range(4*200001+1))
sum_seg = list(0 for _ in range(4*200001+1))
mod = 1000000007


def make_cnt_seg(left, right, loc, idx):
    global cnt_seg
    if left == right:
        cnt_seg[idx] += 1
        return

    cnt_seg[idx] += 1
    mid = (left+right)//2
    if loc <= mid:
        make_cnt_seg(left, mid, loc, idx*2)
    else:
        make_cnt_seg(mid+1, right, loc, idx*2+1)
    return


def make_sum_seg(left, right, loc, idx):
    global sum_seg
    if left == right:
        sum_seg[idx] = (sum_seg[idx] + loc) % mod
        return

    sum_seg[idx] = (sum_seg[idx]+loc) % mod
    mid = (left+right)//2
    if loc <= mid:
        make_sum_seg(left, mid, loc, idx*2)
    else:
        make_sum_seg(mid+1, right, loc, idx*2+1)
    return


def find_cnt_seg(left, right, start, end, idx):
    if start > right or end < left:
        return 0
    if start <= left and right <= end:
        return cnt_seg[idx]

    mid = (left+right)//2
    return find_cnt_seg(left, mid, start, end, idx*2) \
        + find_cnt_seg(mid+1, right, start, end, idx*2+1)


def find_sum_seg(left, right, start, end, idx):
    if start > right or end < left:
        return 0
    if start <= left and right <= end:
        return sum_seg[idx]

    mid = (left+right)//2
    return find_sum_seg(left, mid, start, end, idx*2) \
        + find_sum_seg(mid+1, right, start, end, idx*2+1)


answer = 1
for i in range(1, n+1):
    if i == 1:
        make_cnt_seg(0, 200000, arr[i], 1)
        make_sum_seg(0, 200000, arr[i], 1)
    else:
        l_cnt = find_cnt_seg(0, 200000, 0, arr[i]-1, 1)
        l_sum = find_sum_seg(0, 200000, 0, arr[i]-1, 1)
        r_cnt = find_cnt_seg(0, 200000, arr[i] + 1, 200000, 1)
        r_sum = find_sum_seg(0, 200000, arr[i] + 1, 200000, 1)

        answer = answer * ((r_sum-(arr[i]*r_cnt)) + ((arr[i]*l_cnt) - l_sum))
        answer %= mod

        make_cnt_seg(0, 200000, arr[i], 1)
        if arr[i] != 0:
            make_sum_seg(0, 200000, arr[i], 1)

print(answer)
