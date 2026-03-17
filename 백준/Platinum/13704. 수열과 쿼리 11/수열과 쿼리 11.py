#13704

import sys
input = sys.stdin.readline
import math

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
n_sqrt = math.sqrt(n)

m = int(input())
answer_list = list()
for i in range(m):
    a, b = map(int, input().split())
    answer_list.append([i, a, b, 0])

answer_list.sort(key=lambda x:(x[1]//n_sqrt, x[2] if x[1]//n_sqrt % 2 == 0 else -x[2]))

prefix_xor = [0] * (n+1)
for i in range(1, n+1):
    prefix_xor[i] = prefix_xor[i-1] ^ arr[i]

count = [0] * (1<<20)
answer = 0

def add(value):
    global answer
    tmp = prefix_xor[value]
    answer += count[tmp ^ k]
    count[tmp] += 1

def remove(value):
    global answer
    tmp = prefix_xor[value]
    count[tmp] -= 1
    answer -= count[tmp  ^ k]


curr_l = 1
curr_r = 0

for p in range(m):
    left = answer_list[p][1]-1
    right = answer_list[p][2]

    while curr_l > left:
        curr_l -= 1
        add(curr_l)
    while curr_r < right:
        curr_r += 1
        add(curr_r)
    while curr_l < left:
        remove(curr_l)
        curr_l += 1
    while curr_r > right:
        remove(curr_r)
        curr_r -= 1

    answer_list[p][3] = answer

answer_list.sort(key=lambda x:(x[0]))
for i in answer_list:
    print(i[3])