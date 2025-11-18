#17408

import sys
input = sys.stdin.readline

def make_seg(seg, arr, seg_index, left, right):
    if left == right:
        seg[seg_index] = [arr[left], 0]
        return

    mid = (left+right)//2
    make_seg(seg, arr, seg_index*2, left, mid)
    make_seg(seg, arr, seg_index*2+1, mid+1, right)
    if seg[seg_index*2][0] == seg[seg_index*2+1][0]:
         seg[seg_index] = [seg[seg_index*2][0], seg[seg_index*2+1][0]]
    elif seg[seg_index*2][0] > seg[seg_index*2+1][0]:
        seg[seg_index][0] = seg[seg_index*2][0]
        seg[seg_index][1] = max(seg[seg_index*2][1], seg[seg_index*2+1][0])
    else:
        seg[seg_index][0] = seg[seg_index*2+1][0]
        seg[seg_index][1] = max(seg[seg_index*2][0], seg[seg_index*2+1][1])
    return

def change_seg(seg, seg_index, index, left, right, value):
    if index < left or index > right:
        return
    
    if left == index and right == index:
        seg[seg_index] = [value, 0]
        return

    mid = (left+right)//2
    if index <= mid:
        change_seg(seg, seg_index*2, index, left, mid, value)
    else:
        change_seg(seg, seg_index*2+1, index, mid+1, right, value)
        
    if seg[seg_index*2][0] == seg[seg_index*2+1][0]:
        seg[seg_index] = [seg[seg_index*2][0], seg[seg_index*2+1][0]]

    elif seg[seg_index*2][0] > seg[seg_index*2+1][0]:
        seg[seg_index][0] = seg[seg_index*2][0]
        seg[seg_index][1] = max(seg[seg_index*2][1], seg[seg_index*2+1][0])
    else:
        seg[seg_index][0] = seg[seg_index*2+1][0]
        seg[seg_index][1] = max(seg[seg_index*2][0], seg[seg_index*2+1][1])
    
    return

def find_seg(seg, seg_index, left, right, left_edge, right_edge):
    if right < left_edge or left > right_edge:
        return [0, 0]
    
    if left == right:
        return seg[seg_index]
    
    if left_edge<=left and right <= right_edge:
        return seg[seg_index]
    
    mid = (left+right)//2
    if mid < left_edge:
        return find_seg(seg, seg_index*2+1, mid+1, right, left_edge, right_edge)
    elif mid > right_edge:
        return find_seg(seg, seg_index*2, left, mid, left_edge, right_edge)

    else:
        l = find_seg(seg, seg_index*2, left, mid, left_edge, right_edge)
        r = find_seg(seg, seg_index*2+1, mid+1, right, left_edge, right_edge)
        t = l+r
        t.sort(reverse= True)
        return t[:2]

    

n = int(input())
arr = [0] + list(map(int, input().split()))

seg = list([0, 0] for _ in range(4*n))
make_seg(seg,arr, 1, 1, n )

for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        change_seg(seg, 1, temp[1], 1, n, temp[2])
    else:
        print(sum(find_seg(seg, 1, 1, n, temp[1], temp[2])))