# 1874

import sys
input = sys.stdin.readline

n = int(input())
k = 1
stack = list()
answer = list()

for _ in range(n):
    temp = int(input())

    if len(stack) == 0:
        stack.append(k)
        answer.append('+')
        k += 1

    while stack[-1] < temp:
        stack.append(k)
        answer.append('+')
        k += 1

    while True:
        if stack[-1] == temp:
            stack.pop()
            answer.append('-')
            break
        else:
            stack.pop()

        if len(stack) == 0:
            answer = ['NO']
            break

for i in answer:
    print(i)
