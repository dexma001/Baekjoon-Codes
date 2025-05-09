# 5419

import sys
input = sys.stdin.readline


def update_seg(start, end, idx, index, value):
    if end < index or start > index:
        return 0
    if start == index and index == end:
        seg[idx] += value
        return

    seg[idx] += 1
    mid = (start+end)//2
    if start <= index <= mid:
        update_seg(start, mid, idx*2, index, value)
    else:
        update_seg(mid+1, end, idx*2+1, index, value)


def find_seg(start, end, left, right, idx):
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    l = find_seg(start, mid, left, right, idx*2)
    r = find_seg(mid+1, end, left, right, idx*2+1)
    return l + r


case = int(input())

for _ in range(case):
    n = int(input())
    arr = list()
    y_s = set()
    for _ in range(n):
        temp = list(map(int, input().split()))
        y_s.add(temp[1])
        arr.append(temp)

    y_s = sorted(list(y_s), reverse=True)
    seg_size = len(y_s)
    arr.sort(key=lambda x: x[1])
    zip_y = 1
    for i in arr:
        if i[1] == y_s[-1]:
            i[1] = zip_y
        else:
            zip_y += 1
            i[1] = zip_y
            y_s.pop()
    arr.sort(key=lambda x: [x[0], -x[1]])

    seg = list(0 for _ in range(4*seg_size+1))
    answer = 0
    for i, j in arr:
        answer += find_seg(1, seg_size, j, zip_y, 1)
        update_seg(1, seg_size, 1, j, 1)
    print(answer)
