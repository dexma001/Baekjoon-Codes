# 16120

import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
n = len(arr)

stack = list()

for i in range(n):
    stack.append(arr[i])

    while stack and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P']:
    print('PPAP')
else:
    print('NP')
