#32277

import sys
input = sys.stdin.readline
import math
from collections import defaultdict
import time

for case in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    n_sqrt = math.sqrt(n)

    q = int(input())
    answer_list = list()
    for i in range(q):
        l, r = map(int, input().split())
        answer_list.append([i, l, r, 0])

    answer_list.sort(key=lambda x:(x[1] // n_sqrt, x[2] if x[1]//n_sqrt % 2 == 0 else -x[2]))

    count = defaultdict(int)
    answer = 0
    
    def add(value):
        global answer
        while True:
            count[value] += 1
            if value != 1 and count[value] % value == 0:
                answer += 1
                value **= 2
            else:
                break

    def remove(value):
        global answer
        while True:
            if value != 1 and count[value] % value == 0:
                count[value] -= 1
                answer -= 1
                value **= 2

            else:
                count[value] -= 1
                break


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

        answer_list[i][3] = answer

    answer_list.sort(key=lambda x:(x[0]))
    print(f"Case #{case+1}")
    for i in answer_list:
        print(i[3])

