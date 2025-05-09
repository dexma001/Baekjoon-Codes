#11658

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)]]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))
    
seg_len = 1<<math.ceil(math.log2(n))+1
_2D_seg = list([] for _ in range(seg_len))

def make_1D_seg(start, end, _1D_seg, arr_idx , idx):
    if start == end:
        _1D_seg[idx] = arr[arr_idx][start]
        return
    mid = (start+end)//2
    make_1D_seg(start, mid, _1D_seg, arr_idx, idx*2)
    make_1D_seg(mid+1, end, _1D_seg, arr_idx, idx*2+1)        
    _1D_seg[idx] = _1D_seg[idx*2] + _1D_seg[idx*2+1]
    return _1D_seg

def make_2D_seg(start, end, idx):
    if start == end:
        temp = list(0 for _ in range(seg_len))
        _2D_seg[idx] = make_1D_seg(1, n, temp, start, 1)
        return
    
    mid = (start+end)//2
    make_2D_seg(start, mid, idx*2)
    make_2D_seg(mid+1, end, idx*2+1)
    for i in range(seg_len):
        _2D_seg[idx].append(_2D_seg[idx*2][i] + _2D_seg[idx*2+1][i])

make_2D_seg(1, n, 1)

def update_1D(start, end, arr_idx, dy, dx ,value, idx):
    if start == end:
        _2D_seg[arr_idx][idx] += (value - arr[dy][dx])
        return
    
    _2D_seg[arr_idx][idx] += (value - arr[dy][dx])
    mid = (start+end)//2
    if start <= dx <= mid:
        update_1D(start, mid, arr_idx, dy, dx, value, idx*2)
    else:
        update_1D(mid+1, end, arr_idx, dy, dx, value, idx*2+1)
        
def update_2D(start, end, dy, dx, value, idx):
    if start == end:
        update_1D(1, n, idx, dy, dx, value, 1)
        return
    
    mid = (start+end)//2
    if start<=dy<=mid:
        update_1D(1, n, idx, dy, dx, value, 1)
        update_2D(start, mid, dy, dx, value, idx*2)
    else:
        update_1D(1, n, idx, dy, dx, value, 1)
        update_2D(mid+1, end, dy, dx, value, idx*2+1)
    
def find_1D(start, end, st_y, st_x, end_y, end_x, _2D_idx, idx):   
    if end < st_x or start > end_x:
        return 0
    
    if st_x<=start and end <= end_x:
        return _2D_seg[_2D_idx][idx]

    mid = (start+end)//2
    l1 = find_1D(start, mid, st_y, st_x, end_y, end_x, _2D_idx, idx*2)
    r1 = find_1D(mid+1, end, st_y, st_x, end_y, end_x, _2D_idx, idx*2+1)
    return l1 + r1
    
def find_2D(start, end, st_y, st_x, end_y, end_x, idx):
    if end < st_y or start > end_y:
        return 0
        
    if st_y<=start and end <=end_y:
        return find_1D(1, n, st_y, st_x, end_y, end_x, idx, 1)
        
    mid = (start+end)//2
    l = find_2D(start, mid, st_y, st_x, end_y, end_x, idx*2)
    r = find_2D(mid+1, end, st_y, st_x, end_y, end_x, idx*2+1)
    return l + r 

for _ in range(m):
    cal = list(map(int, input().split()))
    if cal[0] == 0:
        update_2D(1, n, cal[1], cal[2], cal[3], 1)
        arr[cal[1]][cal[2]] = cal[3]
    else:
        print(find_2D(1, n, cal[1], cal[2], cal[3], cal[4], 1))