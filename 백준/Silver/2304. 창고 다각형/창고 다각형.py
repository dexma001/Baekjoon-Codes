# 2304

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort()

stack = list()

answer = 0
for i in range(n):
    if not stack:
        stack.append(arr[i])
        continue

    if arr[i][1] > stack[0][1]:
        while stack and stack[0][1] < arr[i][1]:
            a, b = stack.pop()
        answer += b*(arr[i][0] - a)
        stack.append(arr[i])

    else:
        stack.append(arr[i])

p, q = stack.pop()

while stack:
    a, b = stack.pop()
    if q <= b:
        answer += q*(p-a)
        p, q = a, b

answer += q
print(answer)
