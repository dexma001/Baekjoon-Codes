# 2357 - bottom up

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))

size = 1
while size < n:
    size <<= 1
segment_tree = list()
for _ in range(2*size):
    segment_tree.append([10**10, 0])
size -= 1


def update(idx, diff):
    idx += size
    while idx:
        segment_tree[idx] = [min(segment_tree[idx][0], diff), max(
            segment_tree[idx][1], diff)]
        idx //= 2


for i in range(1, n+1):
    update(i, arr[i-1])


def segment_search(left, right):
    while left <= right:
        if left % 2 == 1:
            answer_arr[0] = min(answer_arr[0], segment_tree[left][0])
            answer_arr[1] = max(answer_arr[1], segment_tree[left][1])
            left += 1
        left //= 2

        if right % 2 == 0:
            answer_arr[0] = min(answer_arr[0], segment_tree[right][0])
            answer_arr[1] = max(answer_arr[1], segment_tree[right][1])
            right -= 1
        right //= 2


for _ in range(m):
    a, b = map(int, input().split())
    answer_arr = [10**10, 0]
    segment_search(a+size, b+size)
    print(*answer_arr)
