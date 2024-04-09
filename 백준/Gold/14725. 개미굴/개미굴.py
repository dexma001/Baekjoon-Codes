# 14725

import sys
input = sys.stdin.readline

n = int(input())
all_tree = list()

for _ in range(n):
    arr = list(map(str, input().split()))[1:]
    all_tree.append(arr)

all_tree.sort()

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

for i in answer:
    print(i)
