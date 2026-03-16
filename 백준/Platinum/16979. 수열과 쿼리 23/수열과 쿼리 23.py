#16979

import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())
ar = list(map(int, input().split()))
n_sqrt = math.sqrt(n)

dic = {v: i+1 for i, v in enumerate(sorted(set(ar)))}
arr = [0] + [dic[j] for j in ar]

answer_list = list()
for i in range(m):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0])

answer_list.sort(key=lambda x:(x[1]//n_sqrt, x[2] if x[1]//n_sqrt % 2 == 0 else -x[2]))

seg_tree = [0] * (2*100000+2)
answer = 0

def find(left, right):
    left += 100000
    right += 100000
    tmp = 0

    while left <= right:
        if left % 2 == 1:
            tmp += seg_tree[left]
            left += 1
        if right % 2 == 0:
            tmp += seg_tree[right]
            right -= 1
        left //= 2
        right //= 2
        
    return tmp

def update(idx, diff):
    idx += 100000
    seg_tree[idx] += diff

    while idx > 1:
        idx //= 2
        seg_tree[idx] = seg_tree[idx*2] + seg_tree[idx*2+1]

curr_l = answer_list[0][1]
curr_r = answer_list[0][1] - 1

for i in range(m):
    left = answer_list[i][1]
    right = answer_list[i][2]

    while left < curr_l:
        curr_l -= 1
        answer += find(1, arr[curr_l] - 1)
        update(arr[curr_l], 1)


    while right > curr_r:
        curr_r += 1
        answer += find(arr[curr_r] + 1, 100000)
        update(arr[curr_r], 1)


    while left > curr_l:
        update(arr[curr_l], -1)
        answer -= find(1, arr[curr_l] - 1)
        curr_l += 1

    while curr_r > right:
        update(arr[curr_r], -1)
        answer -= find(arr[curr_r] + 1, 100000)
        curr_r -= 1

    answer_list[i][3] = answer

answer_list.sort(key=lambda x:(x[0]))
for i in answer_list:
    print(i[3])