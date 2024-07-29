# 26042

from collections import deque
import sys
input = sys.stdin.readline

stack = deque([])

answer = [0, 0]
for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        stack.append(temp[1])

        if len(stack) > answer[0]:
            answer = [len(stack), stack[-1]]

        if len(stack) == answer[0]:
            if stack[-1] < answer[1]:
                answer = [len(stack), stack[-1]]
    else:
        stack.popleft()

print(*answer)
