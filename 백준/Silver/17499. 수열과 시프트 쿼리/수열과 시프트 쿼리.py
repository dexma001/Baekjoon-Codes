# 17499

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
li = deque(list(map(int, input().split())))
p = 0

for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        li[(p+cmd[1]-1) % n] += cmd[2]
    elif cmd[0] == 2:
        p -= cmd[1]
    else:
        p += cmd[1]

for i in range(p, p+n):
    print(li[i % n], end=' ')
