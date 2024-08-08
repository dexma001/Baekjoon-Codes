# 17952

import sys
input = sys.stdin.readline

time = int(input())
stack = list()
answer = 0

for _ in range(time):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                answer += stack[-1][0]
                stack.pop()
    else:
        if temp[2] == 1:
            answer += temp[1]
        else:
            stack.append([temp[1], temp[2]-1])

print(answer)
