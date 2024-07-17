# 27445

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1 and m == 1:
    print(1, 1)

elif n == 1:
    answer = [1, 1]
    arr = list(map(int, input().split()))
    temp = arr[0]
    for i in range(1, m):
        if arr[i] < temp:
            temp = arr[i]
            answer[1] = i+1
    print(*answer)
else:

    answer_loc = [10**10, 10**10]
    answer = [1, 1]

    answer_loc[0] = int(input())
    for i in range(n-2):
        temp = int(input())
        if temp < answer_loc[0]:
            answer_loc[0] = temp
            answer[0] = i+2

    arr = list(map(int, input().split()))

    if arr[0] < answer_loc[0]:
        answer[0] = n

    for i in range(0, m):
        if arr[i] < answer_loc[1]:
            answer_loc[1] = arr[i]
            answer[1] = i+1

    print(*answer)
