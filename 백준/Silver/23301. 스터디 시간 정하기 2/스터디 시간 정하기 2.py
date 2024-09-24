# 23301

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(0 for i in range(1001))

for _ in range(n):
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for i in range(a+1, b+1):
            arr[i] += 1

answer = [sum(arr[1:m+1]), [0, m]]
temp_answer = sum(arr[1:m+1])

for i in range(m+1, 1000):
    temp_answer -= arr[i-m]
    temp_answer += arr[i]
    if temp_answer > answer[0]:
        answer = [temp_answer, [i - m, i]]

print(*answer[1])
