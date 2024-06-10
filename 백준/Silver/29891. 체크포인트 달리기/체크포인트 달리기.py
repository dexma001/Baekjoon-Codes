# 29891

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_plus = list()
arr_minus = list()

for _ in range(n):
    temp = int(input())
    if temp >= 0:
        arr_plus.append(temp)
    else:
        arr_minus.append(-temp)

arr_plus.sort(reverse=True)
arr_minus.sort(reverse=True)

answer = 0
for i in range(0, len(arr_plus), m):
    answer += arr_plus[i] * 2

for i in range(0, len(arr_minus), m):
    answer += arr_minus[i] * 2

print(answer)
