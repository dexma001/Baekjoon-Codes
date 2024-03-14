# 16928

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
shortcut = dict()
trig = set()

for _ in range(n+m):
    a, b = map(int, input().split())
    shortcut[a] = b
    trig.add(a)

queue = deque()
queue.append((1, 0))

plus_term = [1, 2, 3, 4, 5, 6]
delete_list = set()

breaker = 0
while queue:
    x, y = queue.popleft()

    for i in range(6):
        if x + plus_term[i] in delete_list:
            continue

        x1 = x + plus_term[i]

        if x1 == 100:
            print(y+1)
            breaker = 1
            break

        if x1 in trig:
            x1 = shortcut[x1]

        cand = (x1, y+1)

        queue.append(cand)
        delete_list.add(x1)

    if breaker == 1:
        break
