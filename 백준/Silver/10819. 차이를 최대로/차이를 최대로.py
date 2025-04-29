# 10819

from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0  # 최종 답안


def back_track(temp_answer, last, to_add, arr_except_to_add):
    # last: 재배치한 배열의 마지막 정수
    # to_add: 재배치한 배열의 마지막에 이제 추가할 정수
    # arr_except_to_add: 앞으로 배치할 정수들 중 to_add를 제외한 정수 배열
    global answer
    if len(arr_except_to_add) == 0:  # to_add가 마지막 정수일 때
        temp_answer += abs(last - to_add)
        answer = max(temp_answer, answer)
        return

    if to_add == None:  # 맨 처음에는 to_add를 아직 안정했으므로 last를 to_add로 한다.
        to_add = last
    else:
        temp_answer += abs(last - to_add)

    for j in range(len(arr_except_to_add)):
        # 가지고 있는 원소에서 뭘 뺄지를 BruteForce하고자 하기에 원 배열을 보장하는 deepcopy
        copy_arr = deepcopy(arr_except_to_add)
        new_to_add = copy_arr.pop(j)
        back_track(temp_answer, to_add, new_to_add, copy_arr)


for i in range(N):
    copy_original_arr = deepcopy(arr)
    start_element = copy_original_arr.pop(i)  # 재배치할때 어떤 정수를 시작 정수로 할 것 인지.
    back_track(0, start_element, None, copy_original_arr)

print(answer)
