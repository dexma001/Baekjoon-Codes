# 12789

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

front_stack = list()
end_stack = list()

for i in arr:
    if not end_stack:
        end_stack.append(i)
        continue

    if i < end_stack[-1]:
        end_stack.append(i)

    else:
        while end_stack and end_stack[-1] < i:
            front_stack.append(end_stack.pop())
        end_stack.append(i)

if not front_stack:
    front_stack.append(end_stack.pop())

while end_stack and end_stack[-1] > front_stack[-1]:
    front_stack.append(end_stack.pop())

for i in range(1, n+1):
    if front_stack[i-1] != i:
        print('Sad')
        break
else:
    print('Nice')
