# 10819

from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0


def back_track(temp_answer, last, to_add, arr_except_to_add):
    global answer
    if len(arr_except_to_add) == 0:
        temp_answer += abs(last - to_add)
        answer = max(temp_answer, answer)
        return

    if to_add == None:
        to_add = last
    else:
        temp_answer += abs(last - to_add)

    for j in range(len(arr_except_to_add)):
        copy_arr = deepcopy(arr_except_to_add)
        want_to_add = copy_arr.pop(j)
        back_track(temp_answer, to_add, want_to_add, copy_arr)


for i in range(N):
    copy_ori = deepcopy(arr)
    start = copy_ori.pop(i)
    temp = back_track(0, start, None, copy_ori)

print(answer)
