# 2003

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += arr[j]
        if temp == m:
            answer += 1
            break
        elif temp > m:
            break

print(answer)
