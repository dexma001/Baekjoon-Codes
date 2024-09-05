# 12847

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = list()

temp = 0
for i in range(m):
    temp += arr[i]

answer.append(temp)
for i in range(m, n):
    temp = answer[-1] - arr[i-m] + arr[i]
    answer.append(temp)

print(max(answer))
