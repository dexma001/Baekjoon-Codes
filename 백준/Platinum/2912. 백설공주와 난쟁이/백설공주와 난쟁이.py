#2912

import random
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [0] + list(map(int, input().split()))

m = int(input())
answer_arr = list()
for i in range(m):
    a, b = map(int, input().split())
    answer_arr.append([i, a, b, a//int(n**0.5), ''])

answer_arr.sort(key=lambda x:[x[3], x[2]])

color = list(0 for _ in range(10001))
count = list(0 for _ in range(300001))
max_color_cnt = 0

def add(t):
    global max_color_cnt

    if color[t] > 0:
        count[color[t]] -= 1


    color[t] += 1
    count[color[t]] += 1
    if color[t] > max_color_cnt:
        max_color_cnt = color[t]

def delete(t):
    global max_color_cnt

    count[color[t]] -= 1

    if color[t] == max_color_cnt and count[color[t]] == 0:
        max_color_cnt -= 1

    color[t] -= 1
    if color[t] > 0:
        count[color[t]] += 1

curr_l = answer_arr[0][1]
curr_r = answer_arr[0][1] - 1

for q in range(m):
    target_l = answer_arr[q][1]
    target_r = answer_arr[q][2]

    while curr_l > target_l:
        curr_l -= 1
        add(arr[curr_l])
    while curr_r < target_r:
        curr_r += 1
        add(arr[curr_r])

    while curr_l < target_l:
        delete(arr[curr_l])
        curr_l += 1
    while curr_r > target_r:
        delete(arr[curr_r])
        curr_r -= 1

    if max_color_cnt > (target_r - target_l + 1)//2:
        while True:
            t = random.randint(target_l, target_r )
            if color[arr[t]]  == max_color_cnt:
                answer_arr[q][4] = f"yes {arr[t]}"
                break
    else:
            answer_arr[q][4] = "no"

answer_arr.sort(key=lambda x:[x[0]])
for i in answer_arr:
    print(i[-1])