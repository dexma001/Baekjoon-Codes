# 9935

import sys
input = sys.stdin.readline

string = str(input().rstrip())
bomb = str(input().rstrip())

string_list = list(i for i in string)
bomb_list = list(j for j in bomb)
length = len(bomb_list)

stack = list()
for i in string_list:
    stack.append(i)
    if stack[-1] == bomb_list[-1]:
        if (''.join(stack[-length:])) == (''.join(bomb)):
            for i in range(length):
                stack.pop()

if len(stack) != 0:
    print(''.join(stack))
else:
    print('FRULA')
