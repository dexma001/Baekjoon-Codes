# 2812

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(str, input().rstrip()))

stack = list()

time = 0

for i in range(n):
    if time > m:
        stack.append(arr[i])
        continue

    if not stack:
        stack.append(arr[i])

    else:
        while stack and int(arr[i]) > int(stack[-1]) and time < m:
            stack.pop()
            time += 1
        stack.append(arr[i])

while time < m:
    stack.pop()
    time += 1

print(''.join(stack))
