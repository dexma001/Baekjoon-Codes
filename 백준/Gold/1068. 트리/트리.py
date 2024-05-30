# 1068

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
minus = int(input())

tree = list([] for _ in range(n))
root_node = 0
for i in range(n):
    if arr[i] == -1:
        root_node = i
    else:
        tree[i].append(arr[i])
        tree[arr[i]].append(i)

visited = [False] * n
stack = []
stack.append(root_node)
answer = 0

if root_node == minus:
    print(0)
else:
    while stack:
        for i in range(len(stack)):
            temp = stack.pop(0)
            if visited[temp] == True:
                continue
            else:
                visited[temp] = True
                for i in tree[temp]:
                    if i == minus:
                        if len(tree[temp]) == 1:
                            answer += 1
                        else:
                            continue
                    elif len(tree[i]) == 1:
                        answer += 1
                    else:
                        stack.append(i)
                        tree[i].remove(temp)

    print(answer)
