# 10798

import sys
input = sys.stdin.readline

arr = list()
arr_len = list()
max_len = 0
for _ in range(5):
    temp = list(map(str, input().rstrip()))
    arr.append(temp)
    arr_len.append(len(temp))
    max_len = max(len(temp), max_len)

answer = list()
for i in range(max_len):
    for j in range(5):
        if i+1 <= arr_len[j]:
            answer.append(arr[j][i])

print(''.join(answer))
