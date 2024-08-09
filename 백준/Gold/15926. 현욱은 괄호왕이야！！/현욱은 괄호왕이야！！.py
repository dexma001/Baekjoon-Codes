# 15926

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().rstrip()))

stack = list()
counter = list(0 for _ in range(n+1))

for i in range(n):
    if arr[i] == '(':
        stack.append(i)
    else:
        if stack:
            counter[i] = counter[stack[-1]] = 1
            stack.pop()

ans = 0
cnt = 0
for i in counter:
    if i == 1:
        cnt += 1
        ans = max(cnt, ans)
    else:
        cnt = 0

print(ans)
