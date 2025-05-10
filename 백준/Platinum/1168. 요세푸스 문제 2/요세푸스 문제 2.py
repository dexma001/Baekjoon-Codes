#1168

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

seg = list(0 for _ in range(4*n))
answer = list()

def make_seg(start, end, idx):
    if start == end:
        seg[idx] = 1
        return seg[idx]
    
    mid = (start+end)//2
    make_seg(start, mid, idx*2)
    make_seg(mid+1, end, idx*2+1)
    seg[idx] = seg[idx*2] + seg[idx*2+1]
    
make_seg(1, n, 1)

def update_seg(start, end, index, idx):
    if start == end:
        seg[idx] -= 1
        return

    seg[idx] -= 1
    mid = (start+end)//2
    if start<=index<=mid:
        update_seg(start, mid, index, idx*2)
    else:
        update_seg(mid+1, end, index, idx*2+1)
        
def find_seg(start, end, value, idx):
    if start == end:
        return start
    
    mid = (start+end)//2
    if value <= seg[idx*2]:
        return find_seg(start, mid, value, idx*2)
    else:
        return find_seg(mid+1, end, value - seg[idx*2], idx*2+1)
    
start = 1

for i in range(n):
    size = n-i
    start += (k - 1)

    if start % size == 0:
        start = size
    elif start > size:
        start %= size

    ans = find_seg(1, n, start, 1)
    answer.append(str(ans))
    update_seg(1, n, ans, 1)

print('<' +', '.join(answer)+'>')