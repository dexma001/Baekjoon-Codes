# 2828

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

start = 1
end = m
answer = 0

for _ in range(j):
    temp = int(input())
    if start <= temp <= end:
        continue

    if temp < start:
        answer += (start-temp)
        start = temp
        end = temp+m-1

    else:
        answer += (temp - end)
        end = temp
        start = temp - m + 1

print(answer)
