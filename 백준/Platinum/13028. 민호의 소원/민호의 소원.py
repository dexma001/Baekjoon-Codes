#13028

import sys
input = sys.stdin.readline
import math

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer_list = list()
tmp = math.sqrt(n)
for i in range(q):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0, a//tmp])

answer_list.sort(key=lambda x:(x[4], x[2] if x[4] % 2 == 0 else -x[2]))

number = list(0 for _ in range(100001))
ox = list(0 for _ in range(100001))
max_cnt = 0

curr_l = answer_list[0][1]
curr_r = answer_list[0][1] - 1

def add(value):
    global max_cnt

    number[value] += 1
    if 3 <= number[value] and not ox[value]:
        max_cnt += 1
        ox[value] = 1

def remove(value):
    global max_cnt

    if number[value] == 3 and ox[value]:
        max_cnt -= 1
        ox[value] = 0

    number[value] -= 1


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

    answer_list[i][3] = max_cnt

answer_list.sort(key=lambda x:(x[0]))

for i in answer_list:
    print(i[3])
