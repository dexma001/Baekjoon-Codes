import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

nge = [-1] * n
stack = []

for i in range(n):
    while stack and li[stack[-1]] < li[i]:
        nge[stack.pop()] = li[i]
    stack.append(i)

print(*nge)
