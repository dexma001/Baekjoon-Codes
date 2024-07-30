# 2104

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))+[0]
perfix_sum = list(0 for _ in range(n+1))
for i in range(n):
    perfix_sum[i+1] = perfix_sum[i] + arr[i]

answer = 0
stack = deque([])
for i in range(n+1):
    idx = arr[i]
    j = i
    while stack and stack[-1][0] >= arr[i]:
        height, j = stack.pop()
        temp_answer = (perfix_sum[i] - perfix_sum[j])*height
        answer = max(answer, temp_answer)
    stack.append([idx, j])

print(answer)
