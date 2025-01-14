# 11578

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
tot = (1 << n)-1
answer = -1

for _ in range(m):
    temp = list(map(int, input().split()))[1:]
    t = 0
    for i in temp:
        t |= 1 << (i-1)

    if t & tot == tot:
        answer = 1
    arr.append(t)


for i in range(2, m+1):
    if answer != -1:
        break
    p = list(itertools.combinations(list(j for j in range(1, m+1)), i))

    for j in p:
        temp_answer = 0
        for k in j:
            temp_answer |= arr[k-1]
        if temp_answer & tot == tot:
            answer = i

print(answer)
