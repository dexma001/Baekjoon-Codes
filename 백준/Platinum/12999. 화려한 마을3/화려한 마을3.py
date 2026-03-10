#12999

import sys
import math
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer_list = list()
t = math.sqrt(n)
for i in range(q):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0, a//t])
    
answer_list.sort(key=lambda x:(x[4], -x[2] if x[4]%2 == 0 else x[2]))

paint = [0] * 200001
cnt = [0] * 100001
max_cnt = 0

def add(value):
    global max_cnt
    cnt[paint[value]] -= 1
    
    paint[value] += 1
    if paint[value] > max_cnt:
        max_cnt = paint[value]
    cnt[paint[value]] += 1
        
def delete(value):
    global max_cnt 
    
    if max_cnt == paint[value] and cnt[paint[value]] == 1:
        max_cnt -= 1
        
    cnt[paint[value]] -= 1
    paint[value] -= 1
    if paint[value]:
        cnt[paint[value]] += 1

curr_l = answer_list[0][1]
curr_r = answer_list[0][1] - 1
for i in range(q):
    while curr_l > answer_list[i][1]:
        curr_l -= 1
        add(arr[curr_l])
    while curr_r < answer_list[i][2]:
        curr_r += 1
        add(arr[curr_r])
    while curr_l < answer_list[i][1]:
        delete(arr[curr_l])
        curr_l += 1
    while curr_r > answer_list[i][2]:
        delete(arr[curr_r])
        curr_r -= 1
        
    answer_list[i][3] = max_cnt
    
answer_list.sort(key=lambda x:(x[0]))
for i in range(q):
    print(answer_list[i][3])
    