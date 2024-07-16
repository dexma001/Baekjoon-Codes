# 17413

import sys
input = sys.stdin.readline

arr = list(input().rstrip())

answer = list()
stack = list()
switch = 0
for i in range(len(arr)):
    if arr[i] == '<':
        if stack:
            stack.reverse()
            for j in stack:
                answer.append(j)
            stack.clear()
        answer.append(arr[i])
        switch = 1

    elif arr[i] == '>':
        answer.append(arr[i])
        switch = 0

    else:
        if switch == 1:
            answer.append(arr[i])
        elif arr[i] == ' ':
            stack.reverse()
            for j in stack:
                answer.append(j)
            stack.clear()
            answer.append(' ')
        else:
            stack.append(arr[i])

if stack:
    stack.reverse()
    for j in stack:
        answer.append(j)

print(''.join(answer))
