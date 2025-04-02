# 1213

import sys
from collections import defaultdict
input = sys.stdin.readline

name = str(input().strip())
temp = defaultdict(int)

for i in name:
    temp[i] += 1

temp_values = list(temp.values())
how_many_odd = 0

for i in temp_values:
    if i % 2 != 0:
        how_many_odd += 1

if how_many_odd >= 2:
    print("I'm Sorry Hansoo")
    quit()

ttemp = list(temp.items())
ttemp.sort(key=lambda x: x[0])

odd = ''
left_answer = ''
right_answer = ''

for i, j in ttemp:
    if j % 2 != 0:
        if j == 1:
            odd = i
        else:
            odd = i
            left_answer += i*((j-1)//2)
            right_answer += i*((j-1)//2)
    else:
        left_answer += i*(j//2)
        right_answer += i*(j//2)

right_answer = right_answer[::-1]

print(left_answer+right_answer) if odd == '' else print(left_answer+odd+right_answer)
