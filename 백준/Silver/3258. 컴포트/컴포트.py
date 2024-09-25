# 3258

import time
from collections import deque
import sys
input = sys.stdin.readline

n, z, m = map(int, input().split())
warn = list(map(int, input().split()))

k = 1
while True:
    temp = 1
    visited = list(False for _ in range(n+1))
    visited[1] = True

    while True:
        if temp == z:
            print(k)
            quit()

        temp += k
        if temp != n:
            temp = temp % n

        if visited[temp] == True or temp in warn:
            break
        else:
            visited[temp] = True
    k += 1
