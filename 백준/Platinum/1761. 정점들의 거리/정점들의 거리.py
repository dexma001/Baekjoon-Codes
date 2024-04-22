# 1761

import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
distance = [dict() for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[a][b] = c
    distance[b][a] = c

tree_level_check = [0] * (n+1)
tree_level = [0] * (n+1)
parent = [0] * (n+1)


def cnt_tree_level(x, level):
    tree_level_check[x] = 1
    tree_level[x] = level
    for i in graph[x]:
        if tree_level_check[i] == 1:
            continue
        parent[i] = x
        cnt_tree_level(i, level + 1)


cnt_tree_level(1, 1)

Sparse_table = list()
Sparse_table.append(parent)
level = math.ceil(math.log(max(tree_level), 2))
for i in range(level-1):
    Sparse_table.append([0] * (n+1))
    for j in range(n):
        Sparse_table[i+1][j+1] = Sparse_table[i][Sparse_table[i][j+1]]
        if Sparse_table[i+1][j+1] != 0:
            x = (j+1)
            y = Sparse_table[i+1][j+1]
            z = distance[j+1][Sparse_table[i][j+1]] + \
                distance[Sparse_table[i][j+1]][y]
            distance[x][y] = z
            distance[y][x] = z

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b in distance[a].keys():
        print(distance[a][b])
    else:
        answer = 0
        if tree_level[a] < tree_level[b]:
            a, b = b, a
        while tree_level[a] != tree_level[b]:
            for i in range(level-1, -1, -1):
                if tree_level[Sparse_table[i][a]] < tree_level[b]:
                    continue
                else:
                    answer += distance[a][Sparse_table[i][a]]
                    a = Sparse_table[i][a]
                    break

        if a == b:
            print(answer)
        else:
            for i in range(level-1, -1, -1):
                if Sparse_table[i][a] != 0 and Sparse_table[i][a] != Sparse_table[i][b]:
                    answer += distance[a][Sparse_table[i][a]
                                          ] + distance[b][Sparse_table[i][b]]
                    a = Sparse_table[i][a]
                    b = Sparse_table[i][b]
            print(answer + distance[a][Sparse_table[0]
                  [a]] + distance[b][Sparse_table[i][b]])
