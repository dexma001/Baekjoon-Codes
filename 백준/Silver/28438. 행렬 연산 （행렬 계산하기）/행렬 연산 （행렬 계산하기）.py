# 28438

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, q = map(int, input().split())

row = defaultdict(int)
column = defaultdict(int)

for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        row[temp[1]] += temp[2]
    else:
        column[temp[1]] += temp[2]

for i in range(1, n+1):
    answer = list()
    for j in range(1, m+1):
        answer.append(row[i] + column[j])
    print(*answer)
