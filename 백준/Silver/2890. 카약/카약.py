#2890

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
answer_temp = list()

for i in range(r):
    temp = list(map(str, input().strip()))
    temp = temp[1:-1]
    
    for j in range(c-3, -1, -1):
        if temp[j] != '.':
            answer_temp.append([temp[j], c-3-j])
            break

rank = 1
answer_temp.sort(key=lambda x:x[1])
answer_temp[0].append(rank)

for i in range(1, 9):
    if answer_temp[i][1] == answer_temp[i-1][1]:
        answer_temp[i].append(rank)
    else:
        rank += 1
        answer_temp[i].append(rank)

answer_temp.sort(key=lambda x:x[0])
for i in range(9):
    print(answer_temp[i][2])
