#13553

import sys
input = sys.stdin.readline
import math

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

m = int(input())
answer_list = list()
tmp = math.sqrt(n)
for i in range(m):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0, a//tmp])

answer_list.sort(key=lambda x:(x[4], x[2] if x[4] % 2 == 0 else -x[2]))

seg = [0] * (2*100001)
answer = 0

def find(left, right):
    left += 100001
    right += 100001
    res = 0

    while left <= right:
        if left % 2 == 1:
            res += seg[left]
            left += 1
        
        if right % 2 == 0:
            res += seg[right]
            right -= 1

        left //= 2
        right //= 2

    return res

def update(idx, diff):
    idx += 100001
    seg[idx] += diff

    while idx > 1:
        idx //= 2
        seg[idx] = seg[idx*2] + seg[idx*2+1]

curr_l = answer_list[0][1]
curr_r = answer_list[0][1] - 1

for i in range(m):
    left = answer_list[i][1]
    right = answer_list[i][2]

    while curr_l > left:
        curr_l -= 1
        val = arr[curr_l] 
        ql = val - k if val - k >= 0 else 0
        qr = val + k if val + k <= 100000 else 100000
        answer += find(ql, qr)
        update(val, 1)

    while curr_r < right:
        curr_r += 1
        val = arr[curr_r] 
        ql = val - k if val - k >= 0 else 0
        qr = val + k if val + k <= 100000 else 100000
        answer += find(ql, qr)
        update(val, 1)


    while curr_l < left:
        val = arr[curr_l]
        update(val, -1) 
        ql = val - k if val - k >= 0 else 0
        qr = val + k if val + k <= 100000 else 100000
        answer -= find(ql, qr)
        curr_l += 1
    while curr_r > right:
        val = arr[curr_r]
        update(val, -1) 
        ql = val - k if val - k >= 0 else 0
        qr = val + k if val + k <= 100000 else 100000
        answer -= find(ql, qr)
        curr_r -= 1

    answer_list[i][3] = answer    

answer_list.sort(key=lambda x:(x[0]))
for i in answer_list:
    print(i[3])