# 11003

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

stack = deque([(0, arr[0])])

answer = [arr[0]]

for i in range(1, n):
    if stack[0][0] <= i - m:
        stack.popleft()
    while stack and stack[-1][1] >= arr[i]:
        stack.pop()
    stack.append((i, arr[i]))
    answer.append(stack[0][1])

print(*answer)
