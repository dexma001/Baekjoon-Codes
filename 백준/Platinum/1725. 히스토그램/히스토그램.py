# 1725

import sys
input = sys.stdin.readline

n = int(input())
li = list(int(input()) for _ in range(n))

stack = []
answer = 0
for i in range(n):
    id = i
    while stack and stack[-1][1] > li[i]:
        id, height = stack.pop()
        temp_ans = (i - id) * height
        answer = max(answer, temp_ans)
    stack.append([id, li[i]])

while stack:
    id, height = stack.pop()
    temp_ans = (n - id) * height
    answer = max(answer, temp_ans)

print(answer)
