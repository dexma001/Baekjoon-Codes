# 2473

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer_list = list()
answer = list()

for i in range(n):
    copy_arr = deepcopy(arr)
    temp_answer = list()
    temp_list = list()

    sta = copy_arr.pop(i)
    temp_answer.append(sta)

    sum1 = 10**10
    a = 0
    b = len(copy_arr)-1
    x = 0
    y = 0

    while True:
        if a == b:
            break

        else:
            if abs(sta + copy_arr[a] + copy_arr[b]) < abs(sta + sum1):
                sum1 = copy_arr[a] + copy_arr[b]
                x = a
                y = b

            if sta + copy_arr[a] + copy_arr[b] >= 0:
                b -= 1
            else:
                a += 1

    temp_answer.extend([copy_arr[x], copy_arr[y]])
    answer_list.append(temp_answer)


sta1 = 10**10
for j in answer_list:
    if abs(sum(j)) < sta1:
        answer = j
        sta1 = abs(sum(j))

answer.sort()
print(*answer)
