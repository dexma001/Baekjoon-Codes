#6515

import sys
input = sys.stdin.readline
import math

while True:
    try:
        n, q = map(int, input().split())
        arr = [0] + list(map(int, input().split()))

        answer_list = list()
        tem = math.sqrt(n)
        for i in range(q):
            a, b = map(int, input().split())
            answer_list.append([i, a, b, 0, a//tem])

        answer_list.sort(key=lambda x:(x[4], x[2] if x[4] % 2 == 0 else -x[2]))

        number = list(0 for _ in range(200001))
        count = list(0 for _ in range(100001))
        max_cnt = 0
        curr_l = answer_list[0][1]
        curr_r = answer_list[0][1] - 1

        def add(val):
            global max_cnt
            if count[number[val]] != 0:
                count[number[val]] -= 1

            number[val] += 1
            if number[val] > max_cnt:
                max_cnt = number[val] 

            count[number[val]] += 1

        def remove(val):
            global max_cnt

            if max_cnt == number[val] and count[number[val]] == 1:
                max_cnt -= 1

            count[number[val]] -= 1
            number[val] -= 1
            count[number[val]] += 1

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
                curr_r-= 1

            answer_list[i][3] = max_cnt

        answer_list.sort(key=lambda x:(x[0]))

        for i in answer_list:
            print(i[3])
    except:
        break