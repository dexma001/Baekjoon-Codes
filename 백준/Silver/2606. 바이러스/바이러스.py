# 2606

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
com_virus = [0] * (n+1)
m = int(input())
com_cont = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    com_cont[a].append(b)
    com_cont[b].append(a)

answer = 0
stack = deque([])
stack.append(1)
com_virus[1] = 1

while stack:
    k = stack.popleft()
    answer += 1

    for i in com_cont[k]:
        if com_virus[i] != 1:
            stack.append(i)
            com_virus[i] = 1
        else:
            continue

print(answer - 1)
