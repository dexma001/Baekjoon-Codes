# 1541

import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip().split('-')))

answer = 0

temp = list(map(int, arr[0].split('+')))
answer += sum(temp)
arr.pop(0)

for i in arr:
    temp = list(map(int, i.split('+')))
    answer -= sum(temp)

print(answer)
