# 28086

import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
ope = ['+', '-', '*', '/']
left = ''
right = ''
op = ''

if arr[0] == '-':
    left += arr.pop(0)
while arr:
    a = arr.pop(0)
    if a in ope:
        op = a
        break
    left += a

left = int(left, 8)
right = int(''.join(arr), 8)

if op == '+':
    temp = oct(left+right)
    if temp[0] == '-':
        print('-'+temp[3:])
    else:
        print(temp[2:])
elif op == '-':
    temp = oct(left - right)
    if temp[0] == '-':
        print('-'+temp[3:])
    else:
        print(temp[2:])
elif op == '*':
    temp = oct(left*right)
    if temp[0] == '-':
        print('-'+temp[3:])
    else:
        print(temp[2:])
else:
    if right == 0:
        print('invalid')
    else:
        temp = oct(left//right)
        if temp[0] == '-':
            print('-' + temp[3:])
        else:
            print(temp[2:])
