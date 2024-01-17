# 4386

import math
import sys
input = sys.stdin.readline

n = int(input())
li_point_list = list()
li_line_length = list()
ans = 0

for i in range(n):
    li_point_list.append(list(map(float, input().split())))

for i in range(n):
    for j in range(i+1, n):
        li_line_length.append([(i, j), math.sqrt((li_point_list[j][0]-li_point_list[i][0])
                                                 ** 2+(li_point_list[j][1] - li_point_list[i][1])**2)])

li_line_length.sort(key=lambda x: x[1])

li_parent_son = list(i for i in range(n))


def find(li_parent_son, x):
    if li_parent_son[x] == x:
        return x
    li_parent_son[x] = find(li_parent_son, li_parent_son[x])
    return li_parent_son[x]


def union(li_parent_son, a, b):
    root_a = find(li_parent_son, a)
    root_b = find(li_parent_son, b)

    if root_a < root_b:
        li_parent_son[root_b] = root_a
    else:
        li_parent_son[root_a] = root_b


for i in range(len(li_line_length)):
    a, b = li_line_length[i][0]
    if find(li_parent_son, a) != find(li_parent_son, b):
        union(li_parent_son, a, b)
        ans += li_line_length[i][1]

print(ans)
