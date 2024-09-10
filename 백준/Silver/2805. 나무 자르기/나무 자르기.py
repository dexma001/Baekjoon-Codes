# 2805

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start, end = 1, arr[-1]

while start <= end:
    mid = (start+end)//2
    tree_length = 0

    for i in arr:
        if mid <= i:
            tree_length += (i-mid)

    if tree_length >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
