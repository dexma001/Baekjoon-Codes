# 2493

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

answer = [0]
stack_copy = defaultdict(int)
stack = [arr[1]]
stack_copy[arr[1]] = 1

for i in range(2, n+1):
    stack_copy[arr[i]] = i
    if arr[i] < stack[-1]:
        answer.append(stack_copy[stack[-1]])
        stack.append(arr[i])
    else:
        while stack and stack[-1] < arr[i]:
            stack.pop()

        if not stack:
            answer.append(0)
        else:
            answer.append(stack_copy[stack[-1]])
        stack.append(arr[i])

print(*answer)
