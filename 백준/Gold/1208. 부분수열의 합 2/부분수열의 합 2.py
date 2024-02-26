# 1208 - combination

import sys
from itertools import combinations
input = sys.stdin.readline


def binary_search(a, arr, start, end):
    if start > end:
        return -1
    mid = (start+end) // 2
    if arr[mid] == a:
        return mid
    elif arr[mid] > a:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(a, arr, start, end)


n, s = map(int, input().split())
n_arr = list(map(int, input().split()))
answer = 0

n_arr_left = list(n_arr[0:n//2])
n_arr_right = list(n_arr[n//2:n])

#
n_arr_right_subarr_sum = dict()  # 부분수열의 합 dict(개수 포함)

for i in range(1, len(n_arr_right)+1):
    for j in list(combinations(n_arr_right, i)):
        sum_n_right = sum(j)
        if n_arr_right_subarr_sum.get(sum_n_right, None) != None:
            n_arr_right_subarr_sum[sum_n_right] += 1
        else:
            n_arr_right_subarr_sum[sum_n_right] = 1

n_arr_right_subarr_sum_list = list(
    n_arr_right_subarr_sum.keys())  # 부분수열의 합 list
n_arr_right_subarr_sum_list.sort()

# 이분탐색으로 탐색 가능하게
for x in range(0, len(n_arr_left)+1):
    for y in list(combinations(n_arr_left, x)):
        if y == ():
            answer += n_arr_right_subarr_sum.get(s, 0)
            continue
        sum_n_left = sum(y)
        if sum_n_left == s:
            answer += n_arr_right_subarr_sum.get(0, 0) + 1
        else:
            num = binary_search(
                s-(sum_n_left), n_arr_right_subarr_sum_list, 0, len(n_arr_right_subarr_sum_list)-1)
            if num == -1:
                continue
            else:
                answer += n_arr_right_subarr_sum[n_arr_right_subarr_sum_list[num]]

print(answer)
