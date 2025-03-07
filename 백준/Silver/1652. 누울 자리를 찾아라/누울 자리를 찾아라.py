# 1652

import copy
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    arr.append(list(map(str, input().strip())))

arr_ = copy.deepcopy(arr)
lr, ud = 0, 0

for i in range(n):
    for j in range(n-1):
        if arr[i][j] == '.' and arr[i][j+1] == '.':
            lr += 1
            while j <= n-1 and arr[i][j] == '.':
                arr[i][j] = 'X'
                j += 1

for i in range(n):
    for j in range(n-1):
        if arr_[j][i] == '.' and arr_[j+1][i] == '.':
            ud += 1
            while j <= n-1 and arr_[j][i] == '.':
                arr_[j][i] = 'X'
                j += 1

print(lr, ud)
