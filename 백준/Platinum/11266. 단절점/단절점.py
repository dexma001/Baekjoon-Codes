# 11266

import sys
sys.setrecursionlimit(2**31-1)
input = sys.stdin.readline

tree, node = map(int, input().split())
tree_arr = list([] for _ in range(tree+1))

for _ in range(node):
    a, b = map(int, input().split())
    tree_arr[a].append(b)
    tree_arr[b].append(a)

visited = list(False for _ in range(tree+1))
answer_list = list(0 for _ in range(tree+1))
answer = list()


def dfs(node, is_root):
    visited[0] += 1
    visited[node] = visited[0]
    child_cnt = 0

    min_order = visited[node]

    for i in tree_arr[node]:
        if visited[i]:
            min_order = min(min_order, visited[i])
            continue
        child_cnt += 1
        res = dfs(i, False)
        min_order = min(min_order, res)

        if not is_root and res >= visited[node]:
            answer_list[node] = 1

    if is_root and child_cnt > 1:
        answer_list[node] = 1

    return min_order


for i in range(1, tree+1):
    if not visited[i]:
        dfs(i, True)
    if answer_list[i]:
        answer.append(i)


answer.sort()
print(len(answer))
if answer:
    print(*answer)
