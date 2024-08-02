# 6198

import sys
input = sys.stdin.readline

n = int(input())
stack = list()
stack_len = 0

answer = 0
for _ in range(n):
    temp = int(input())
    if not stack:
        stack.append(temp)
        stack_len += 1

    elif temp >= stack[-1]:
        while stack and stack[-1] <= temp:
            stack.pop()
            stack_len -= 1
            answer += stack_len
        stack.append(temp)
        stack_len += 1

    else:
        stack.append(temp)
        stack_len += 1


while stack:
    stack.pop()
    stack_len -= 1
    answer += stack_len

print(answer)
