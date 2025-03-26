# 1253

import sys
input = sys.stdin.readline

N = int(input())
A_i = list(map(int, input().split()))
A_i.sort()


def two_pointer(start, end, idx, value, arr):
    while True:
        if start == idx:
            start += 1
        if end == idx:
            end -= 1

        if start == end:
            return False

        if arr[start] + arr[end] == value:
            return True
        elif arr[start] + arr[end] > value:
            end -= 1
        else:
            start += 1


answer = 0

for i in range(N):
    if two_pointer(0, N-1, i, A_i[i], A_i):
        answer += 1


print(answer)
