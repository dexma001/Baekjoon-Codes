# 27964

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().split()))
answer_arr = list()

answer = 0
for i in arr:
    if i[-6:] == 'Cheese' and i not in answer_arr:
        answer += 1
        answer_arr.append(i)

print('yummy') if answer >= 4 else print('sad')
