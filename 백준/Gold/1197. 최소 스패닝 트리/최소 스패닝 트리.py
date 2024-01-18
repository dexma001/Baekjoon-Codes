# 1197

import sys
input = sys.stdin.readline

vertex, weight = map(int, input().split())
li_connect = list()
li_parent = [0] + list(i+1 for i in range(vertex))
ans = 0
for _ in range(weight):
    li_connect.append(list(map(int, input().split())))

li_connect.sort(key=lambda x: x[2])

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


for i in range(len(li_connect)):
    a = li_connect[i][0]
    b = li_connect[i][1]

    if find(a) != find(b):
        union(a, b)
        ans += li_connect[i][2]

print(ans)
