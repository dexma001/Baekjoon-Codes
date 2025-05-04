#7469

import sys
input = sys.stdin.readline
import time
from bisect import bisect_left

n, m = map(int, input().split())
q = [0] + list(map(int, input().split()))

seg = list([] for _ in range(4*n))

def merge_sort(left_arr, right_arr, llen, rlen):
    left = 0
    right = 0
    temp = list()
    
    while left < llen and right < rlen:
        if left_arr[left] <= right_arr[right]:
            temp.append(left_arr[left])
            left += 1
        else:
            temp.append(right_arr[right])
            right += 1
    temp += left_arr[left:]
    temp += right_arr[right:]
    return temp

def make_seg(left, right, idx):
    if left == right:
        seg[idx].append(q[left])
        return seg[idx]
    
    mid = (left + right)//2
    make_seg(left, mid, idx*2)
    make_seg(mid+1, right, idx*2+1)
    seg[idx] = merge_sort(seg[idx*2], seg[idx*2+1], len(seg[idx*2]), len(seg[idx*2+1]))
    return seg[idx]

make_seg(1, n, 1)
    

def find_seg(start, end, left, right, idx, arr):
    if left > end or right < start:
        return 
    
    if left<= start and end <= right:
        arr.append(idx)
        return arr
    
    mid = (start+end)//2
    l1 = find_seg(start, mid, left, right, idx*2, arr)
    r1 = find_seg(mid+1, end, left, right, idx*2+1, arr)
    return arr

for _ in range(m):
    i,j,k = map(int, input().split())
    tot_arr = find_seg(1, n, i, j, 1, [])
    
    minim = -10**9
    maxim = 10**9
    ans = minim
    
    while minim < maxim:
        mid = (minim+maxim)//2
        temp = 0
        for i in tot_arr:
            temp += bisect_left(seg[i], mid)
        if temp >= k:
            maxim = mid
        else:
            ans = mid
            minim = mid + 1
        
    print(ans)