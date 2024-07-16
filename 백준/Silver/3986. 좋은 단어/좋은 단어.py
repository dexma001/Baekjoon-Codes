# 3986

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n):
    arr = list(map(str, input().rstrip()))
    stack = list()

    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)

    if not stack:
        answer += 1

print(answer)
