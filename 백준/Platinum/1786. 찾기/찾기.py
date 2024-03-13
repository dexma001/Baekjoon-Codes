# 1786 - kmp

import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
com_arr = list(map(str, input().rstrip()))
answer = 0
answer_arr = list()

pi = [0] * len(com_arr)


def pi_array():
    j = 0
    for i in range(1, len(com_arr)):
        while j > 0 and com_arr[j] != com_arr[i]:
            j = pi[j-1]
        if com_arr[i] == com_arr[j]:
            j += 1
            pi[i] = j


pi_array()

j = 0
for i in range(len(arr)):
    while j > 0 and com_arr[j] != arr[i]:
        j = pi[j-1]
    if com_arr[j] == arr[i]:
        j += 1
        if j == len(com_arr):
            answer += 1
            answer_arr.append(i-j+2)
            j = pi[j-1]

print(answer)
if answer != 0:
    print(*answer_arr)
