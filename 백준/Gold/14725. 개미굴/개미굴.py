# 14725

import sys
input = sys.stdin.readline

n = int(input())
all_tree = list()
all_node = list()

for _ in range(n):
    arr = list(map(str, input().split()))[1:]
    all_tree.append(arr)
    for i in arr:
        if i not in all_node:
            all_node.append(i)

all_tree.sort()
all_node.sort()

answer = list()

for i in range(len(all_tree)):
    if i == 0:
        for j in range(len(all_tree[i])):
            answer.append('--'*j + all_tree[i][j])
    else:
        idx = 0
        for j in range(len(all_tree[i])):
            if all_tree[i-1][j] != all_tree[i][j] or len(all_tree[i-1]) < j:
                break
            else:
                idx += 1
        for k in range(idx, len(all_tree[i])):
            answer.append('--'*k + all_tree[i][k])
'''
    for j in range(1, len(all_tree[i])):
        node = '--'*(j) + all_tree[i][j]
        if node in answer[start]:
            k1 = list(
                filter(lambda x: answer[start][x] == node, range(len(answer[start]))))
            k = k1[-1]
            l = 1
            while j-l >= 0:
                if answer[start][k-l] != '--'*(j-l) + all_tree[i][j-l]:
                    answer[start].append(node)
                    break
                l += 1
        else:
            answer[start].append(node)
'''

for i in answer:
    print(i)
