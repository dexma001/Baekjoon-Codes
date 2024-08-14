# 12846
# Same as 6549 - 히스토그램에서 가장 큰 직사각형


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0
stack = list()

for i in range(n):
    idx = i
    while stack and stack[-1][1] > arr[i]:
        idx, height = stack.pop()
        answer = max(answer, (i-idx)*height)
    stack.append([idx, arr[i]])


while stack:
    idx, height = stack.pop()
    answer = max(answer, (n-idx)*height)


print(answer)
