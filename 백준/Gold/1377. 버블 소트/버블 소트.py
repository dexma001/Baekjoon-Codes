# 1377

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for i in range(n):
    arr.append([i, int(input())])

arr.sort(key=lambda x: x[1])

answer = 0

for j in range(n):
    answer = max(answer, arr[j][0] - j)

print(answer + 1)
