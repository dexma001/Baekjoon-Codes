# 15829

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().rstrip()))

answer = 0
for i in range(n):
    temp = ord(arr[i]) - 96
    answer += temp * (31**i)

print(answer % 1234567891)
