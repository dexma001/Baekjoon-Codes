# 16978

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

query_num = int(input())
update_query = deque([])
answer_query = defaultdict(list)
answer_len = 0

for _ in range(query_num):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        update_query.append(temp[1:])
    else:
        answer_query[temp[1]].append([answer_len] + temp[2:])
        answer_len += 1

answer_list = list(0 for _ in range(answer_len))

seg = list(0 for _ in range(4*n+1))


def make_seg(start, end, idx):
    if start == end:
        seg[idx] = arr[start]
        return seg[idx]

    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = seg[idx*2] + seg[idx*2+1]
    return seg[idx]


make_seg(1, n, 1)


def find_seg(start, end, left, right, idx):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return seg[idx]

    mid = (start+end)//2
    left_value = find_seg(start, mid, left, right, idx*2)
    right_value = find_seg(mid+1, end, left, right, idx*2+1)
    value = (left_value + right_value)
    return value


def update_seg(start, end, idx, value_idx, value):
    if value_idx < start or end < value_idx:
        return

    if start <= value_idx and end >= value_idx:
        seg[idx] = seg[idx] + (value - arr[value_idx])
        if start == end:
            return

    mid = (start+end)//2
    if start <= value_idx and mid >= value_idx:
        update_seg(start, mid, idx*2, value_idx, value)
    else:
        update_seg(mid+1, end, idx*2+1, value_idx, value)


update_number = 0
for _ in range(len(update_query)):
    for index, i, j in answer_query[update_number]:
        answer_list[index] = find_seg(1, n, i, j, 1)

    p, q = update_query.popleft()
    update_seg(1, n, 1, p, q)
    arr[p] = q
    update_number += 1

for index, i, j in answer_query[update_number]:
    answer_list[index] = find_seg(1, n, i, j, 1)

for i in answer_list:
    print(i)
