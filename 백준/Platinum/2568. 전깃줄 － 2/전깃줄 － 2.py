# 2568

import sys
input = sys.stdin.readline

n = int(input())
arr = dict()
arr_sort = list()
arr_end = list()

for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b

arr_sort = sorted(arr.items())
arr_end = list(i[1] for i in arr_sort)


def binary_search(num, arr, start, end):
    if start > end:
        return start

    mid = (start+end) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid-1] < num < arr[mid]:
        return mid
    elif arr[mid] > num:
        return binary_search(num, arr, start, mid-1)
    else:
        return binary_search(num, arr, mid+1, end)


dp = list()
dp.append([0, arr_end[0]])
lis = list([arr_end[0]])


for i in arr_end[1:]:
    if i > lis[-1]:
        lis.append(i)
        dp.append([len(lis)-1, i])
    else:
        j = binary_search(i, lis, 0, len(lis)-1)
        lis[j] = i
        dp.append([j, i])

print(n - len(lis))

answer = list()
last_idx = len(lis) - 1
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        last_idx -= 1
    else:
        answer.append(arr_sort[arr_end.index(dp[i][1])][0])

for i in range(len(answer)):
    print(answer[-i-1])
