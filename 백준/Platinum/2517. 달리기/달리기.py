# 2517

import sys
input = sys.stdin.readline

n = int(input())
arr = list()
answer = list(0 for _ in range(n))

for i in range(n):
    arr.append([i, int(input())])

arr.sort(key=lambda x: x[1])

for j in range(n):
    arr[j][1] = j+1

arr.sort(key=lambda x: x[0])

seg = list(0 for _ in range(2000000+1))


def find_seg(start, end, left, right, idx):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    return (find_seg(start, mid, left, right, idx*2) + find_seg(mid+1, end, left, right, idx*2+1))


def update_seg(start, end, index, value, idx):
    if start == end:
        seg[idx] += value
        return

    seg[idx] += value
    mid = (start+end)//2
    if start <= index <= mid:
        update_seg(start, mid, index, value, idx*2)
    else:
        update_seg(mid+1, end, index, value, idx*2+1)


for i in range(n):
    print(i + 1 - find_seg(1, 500000, 1, arr[i][1], 1))
    update_seg(1, 500000, arr[i][1], 1, 1)
