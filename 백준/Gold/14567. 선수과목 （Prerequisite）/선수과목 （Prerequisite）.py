# 14567

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prerequisite = list([] for _ in range(n+1))
in_direction = list(0 for _ in range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    prerequisite[a].append(b)
    prerequisite[b].append(a)
    in_direction[b] += 1

visited = list(False for _ in range(n+1))
answer = list(0 for _ in range(n+1))

stack = list()
for i in range(1, n+1):
    if in_direction[i] == 0:
        stack.append(i)

time = 0
while stack:
    time += 1
    for i in range(len(stack)):
        temp = stack.pop(0)
        if visited[temp] == True:
            continue
        else:
            visited[temp] = True
            answer[temp] = time
            for j in prerequisite[temp]:
                in_direction[j] -= 1
                if in_direction[j] == 0:
                    stack.append(j)
print(*answer[1:])
