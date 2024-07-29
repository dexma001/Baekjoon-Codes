# 1918

import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
answer = ''

stack = list()
for i in arr:
    if i.isalpha() == True:
        answer += i
    elif i == '(':
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(i)
    else:
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

while stack:
    answer += stack.pop()
print(answer)
