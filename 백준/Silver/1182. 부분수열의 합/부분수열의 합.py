# 1182

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
n_arr = list(map(int, input().split()))
cnt = 0


def brute_force(idx, arr):
    global cnt

    if idx >= n:
        return -1

    arr += n_arr[idx]

    if arr == s:
        cnt += 1

    brute_force(idx+1, arr)

    brute_force(idx+1, arr-n_arr[idx])


brute_force(0, 0)
print(cnt)
