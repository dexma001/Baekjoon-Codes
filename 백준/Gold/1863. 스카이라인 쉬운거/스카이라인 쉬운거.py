# 1863

import sys
input = sys.stdin.readline

n = int(input())
stack = list()
answer = 0

for _ in range(n):
    a, b = map(int, input().split())

    if not stack:
        stack.append(b)
        continue

    if b > stack[-1]:
        stack.append(b)

    else:
        while stack and stack[-1] > b:
            stack.pop()
            answer += 1

        if not stack or stack[-1] < b:
            stack.append(b)
        else:
            continue

for i in stack:
    if i != 0:
        answer += 1

print(answer)
