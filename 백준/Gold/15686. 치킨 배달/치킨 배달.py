import sys
import math
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

li_h = []
li_c = []

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            li_h.append([i, j])
        elif li[i][j] == 2:
            li_c.append([i, j])

li_c_com = []

for k in combinations(li_c, m):
    li_c_com.append(k)


length_a = 100000000000
for q in range(len(li_c_com)):
    length_compare = 0
    for p in range(len(li_h)):
        length_1 = set()
        for r in range(m):
            u = abs(li_h[p][0] - li_c_com[q][r][0])
            v = abs(li_h[p][1] - li_c_com[q][r][1])
            length_1.add(u+v)
        length_compare += min(length_1)
    if length_compare < length_a:
        length_a = length_compare

print(length_a)
