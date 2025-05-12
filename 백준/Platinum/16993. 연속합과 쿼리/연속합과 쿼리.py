# 16993

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
INF = int(-1000*100000 + 1)

seg = list([-INF, -INF, -INF, 0] for _ in range(4*n+1))

# 구간 내 최대 부분합
# 구간 내 시작부터 최대 부분합
# 구간 내 끝부터 최대 부분합
# 구간 전체합


def make_seg(start, end, idx):
    if start == end:
        for i in range(4):
            seg[idx][i] = arr[start]
        return

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx][1] = max(seg[idx*2][1], seg[idx*2][3] + seg[idx*2+1][1])
    seg[idx][2] = max(seg[idx*2+1][2], seg[idx*2+1][3] + seg[idx*2][2])
    seg[idx][3] = seg[idx*2][3] + seg[idx*2+1][3]
    seg[idx][0] = max(seg[idx*2][0], seg[idx*2+1][0],
                      seg[idx*2][2] + seg[idx*2+1][1])


make_seg(1, n, 1)


def find_seg(start, end, left, right, idx):
    if right < start or left > end:
        return [-INF, -INF, -INF, 0]

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    if right <= mid:
        l = find_seg(start, mid, left, right, idx*2)
        return l

    if left >= mid+1:
        r = find_seg(mid+1, end, left, right, idx*2+1)
        return r

    l = find_seg(start, mid, left, right, idx*2)
    r = find_seg(mid+1, end, left, right, idx*2+1)
    temp = [0, 0, 0, 0]
    temp[1] = max(l[1], l[3] + r[1])
    temp[2] = max(r[2], r[3] + l[2])
    temp[3] = l[3] + r[3]
    temp[0] = max(l[0], r[0], l[2] + r[1])
    return temp


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(find_seg(1, n, a, b, 1)[0])
