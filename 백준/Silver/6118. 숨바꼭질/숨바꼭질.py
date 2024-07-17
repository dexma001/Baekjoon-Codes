# 15975

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = list([] for _ in range(n+1))
node = list(0 for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [1]

visited = list(False for _ in range(n+1))
length = 0

while stack:
    for i in range(len(stack)):
        temp = stack.pop(0)
        visited[temp] = True
        node[temp] = length
        for j in graph[temp]:
            if not visited[j] and j not in stack:
                stack.append(j)
    length += 1

length -= 1

answer = [0, length, 0]
for i in range(1, n+1):
    if node[i] == length:
        if answer[0] == 0:
            answer[0] = i
        answer[2] += 1

print(*answer)
