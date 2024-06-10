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
while len(arr_plus) >= m:
    answer += abs(arr_plus[0]) * 2
    arr_plus = arr_plus[m:]
if len(arr_plus) != 0:
    answer += arr_plus[0] * 2

while len(arr_minus) >= m:
    answer += abs(arr_minus[0]) * 2
    arr_minus = arr_minus[m:]
if len(arr_minus) != 0:
    answer += arr_minus[0] * 2

print(answer)
