# 1725 - 히스토그램

import sys
input = sys.stdin.readline

n = int(input())
li = list(int(input()) for _ in range(n))

stack = []
answer = 0

for i in range(n):
    idx = i
    while stack and stack[-1][1] > li[i]:
        idx, height = stack.pop()
        temp_answer = (i - idx) * height
        answer = max(answer, temp_answer)
    stack.append([idx, li[i]])

while stack:
    idx, height = stack.pop()
    temp_answer = (n - idx) * height
    answer = max(answer, temp_answer)

print(answer)
