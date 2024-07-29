# 17608

import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

answer = 0
temp = 0
for i in range(n-1, -1, -1):
    if arr[i] > temp:
        temp = arr[i]
        answer += 1

print(answer)
