# 2887 - 크루스칼

import sys
input = sys.stdin.readline

n = int(input())
li_length = list()
li_parent = list(i for i in range(n))
ans = 0

p_x = list()
p_y = list()
p_z = list()

for i in range(n):
    x, y, z = list(map(int, input().split()))
    p_x.append((x, i))
    p_y.append((y, i))
    p_z.append((z, i))

p_x.sort()
p_y.sort()
p_z.sort()

for i in range(n-1):
    li_length.append((p_x[i+1][0] - p_x[i][0], p_x[i][1], p_x[i+1][1]))
    li_length.append((p_y[i+1][0] - p_y[i][0], p_y[i][1], p_y[i+1][1]))
    li_length.append((p_z[i+1][0] - p_z[i][0], p_z[i][1], p_z[i+1][1]))

li_length.sort()


def find(x):
    if li_parent[x] != x:
        li_parent[x] = find(li_parent[x])
    return li_parent[x]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        li_parent[parent_b] = parent_a
    else:
        li_parent[parent_a] = parent_b


for i in range(len(li_length)):
    length, a, b = li_length[i]
    if find(a) != find(b):
        union(a, b)
        ans += length

print(ans)
