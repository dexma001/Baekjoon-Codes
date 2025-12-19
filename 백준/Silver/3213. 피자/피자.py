import sys
import math
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
temp = defaultdict(int)

for i in range(n):
    arr = list(map(str, input().strip()))
    if arr[0] == '1':
        if arr[-1] == '4':
            temp[1] += 1
        else:
            temp[2] += 1
    else:
        temp[3] += 1
     
answer = 0

if temp[3] >= temp[1]:
    answer = temp[3] + math.ceil(temp[2] / 2)
else:
    answer = temp[3]
    temp[1] -= temp[3]
    answer += temp[2] //2
    temp[2] %= 2
    if temp[2] == 1:
        if temp[1] <= 2:
            answer +=1
        else:
            answer += (1 + math.ceil((temp[1]-2)/4))
    else:
        answer += math.ceil(temp[1]/4)

print(answer)