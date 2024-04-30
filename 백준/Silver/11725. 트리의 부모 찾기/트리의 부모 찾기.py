#11725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
mother_node = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
tree_level = [0 for _ in range(n+1)]
tree_level[1] = 1
tree_level_check = [0 for _ in range(n+1)]
tree_level_check[1] = 1

def tree_level_checking(n, j):
    tree_level[n] = j
    tree_level_check[n] = 1
    for i in tree[n]:
        if tree_level_check[i] != 1:
            tree_level_checking(i, j+1)
            
tree_level_checking(1, 1)

for i in range(2, n+1):
    answer = 0
    answer_tree_level = 10**8
    for j in tree[i]:
        if tree_level[j] < answer_tree_level:
            answer = j
            answer_tree_level = tree_level[j]
    print(answer)