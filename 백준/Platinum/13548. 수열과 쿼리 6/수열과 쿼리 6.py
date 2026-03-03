#13548

import sys
input = sys.stdin.readline
import math

n = int(input())
arr = [0] + list(map(int, input().split()))

m = int(input())
answer_que = list()
for i in range(m):
    temp = list(map(int, input().split()))
    answer_que.append([i] + temp + [0] + [temp[0]//int(math.sqrt(n))])  #index, left, right, value

answer_que.sort(key=lambda x:[x[4], x[2]])

count = list(0 for _ in range(100001))
table = list(0 for _ in range(100001))
max_cnt = 0

def add(v):
    global max_cnt

    c = count[v]
    if c > 0:
        table[c] -= 1

    count[v] += 1
    table[count[v]] += 1

    if count[v] > max_cnt:
        max_cnt = count[v]

def remove(v):
    global max_cnt

    c = count[v]
    table[c] -= 1

    if c == max_cnt and table[c] == 0:
        max_cnt -= 1

    count[v] -= 1
    if count[v] > 0:
        table[count[v]] += 1 

temp_l = answer_que[0][1]
temp_r = answer_que[0][1]-1

for i in range(m):
    target_l = answer_que[i][1]
    target_r = answer_que[i][2]

    while temp_l > target_l:
        temp_l -= 1
        add(arr[temp_l])
    while temp_r < target_r:
        temp_r += 1
        add(arr[temp_r])

    while temp_l < target_l:
        remove(arr[temp_l])
        temp_l += 1
    while temp_r > target_r:
        remove(arr[temp_r])
        temp_r -= 1

    answer_que[i][3] = max_cnt

answer_que.sort(key = lambda x:x[0])

for i in answer_que:
    print(i[3])
