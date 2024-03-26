# 7578 - 3

import sys
input = sys.stdin.readline

n = int(input())
arr_u = [0] + list(map(int, input().split()))
arr_d = [0] + list(map(int, input().split()))

arr_u_dict = dict(zip(arr_u, range(len(arr_u))))
arr_du = list(arr_u_dict[i] for i in arr_d)
arr_du = arr_du[1:]


def add(arr, idx, val):
    idx += 1
    while idx < len(arr):
        arr[idx] += val
        idx += idx & -idx


def query(arr, idx):
    idx += 1
    sum = 0
    while idx:
        sum += arr[idx]
        idx &= idx - 1
    return sum


def CountInversion(arr, n):
    mx = max(arr_du)
    Fenwick_arr = [0] * (mx + 2)
    answer = 0
    for i in range(n):
        add(Fenwick_arr, arr[i], 1)
        answer += i - query(Fenwick_arr, arr[i]) + 1
    return answer


print(CountInversion(arr_du, n))
