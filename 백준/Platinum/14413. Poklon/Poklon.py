#14413

import sys
input = sys.stdin.readline
import math

n, q = map(int, input().split())
ar = list(map(int, input().split()))
n_sqrt = math.sqrt(n)

dic = {v:i for i, v in enumerate(sorted(set(ar)))}
arr = [0] + [dic[j] for j in ar]

answer_list = list()
for i in range(q):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0])

answer_list.sort(key=lambda x:(x[1]//n_sqrt, x[2] if x[1]//n_sqrt % 2 == 0 else -x[2]))

number = [0] * 500001
count = [0] * 500001
answer = 0

def add(value):
    if number[value]:
        count[number[value]] -= 1

    number[value] += 1
    count[number[value]] += 1

def remove(value):
    count[number[value]] -= 1

    number[value] -= 1
    if number[value]:
        count[number[value]] += 1

curr_l = answer_list[0][1]
curr_r = answer_list[0][1] - 1

for i in range(q):
    left = answer_list[i][1]
    right = answer_list[i][2]

    while curr_l > left:
        curr_l -= 1
        add(arr[curr_l])
    
    while curr_r < right:
        curr_r += 1
        add(arr[curr_r])
    
    while curr_l < left:
        remove(arr[curr_l])
        curr_l += 1

    while curr_r > right:
        remove(arr[curr_r])
        curr_r -= 1

    answer_list[i][3] = count[2]

answer_list.sort(key=lambda x:(x[0]))
for i in answer_list:
    print(i[3])