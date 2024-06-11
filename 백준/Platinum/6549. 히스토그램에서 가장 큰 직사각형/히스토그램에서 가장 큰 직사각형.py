# 6549

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    stack_len = arr.pop(0)

    answer = 0
    stack = list()
    for i in range(stack_len):
        idx = i
        while stack and stack[-1][1] > arr[i]:
            idx, height = stack.pop()
            temp_answer = (i-idx)*height
            answer = max(answer, temp_answer)
        stack.append([idx, arr[i]])

    while stack:
        idx, height = stack.pop()
        temp_answer = (stack_len-idx) * height
        answer = max(answer, temp_answer)

    print(answer)
