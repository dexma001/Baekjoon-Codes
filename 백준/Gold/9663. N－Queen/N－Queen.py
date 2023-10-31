import copy
import math
from collections import deque

n = int(input())
li = [0] * n
visited = [False] * n
result = 0


def nqueens(k):
    global result
    if k == n:
        result += 1
        return

    for i in range(n):
        if visited[i] == False:
            li[k] = i

            if check(k):
                visited[i] = True
                nqueens(k + 1)
                visited[i] = False


def check(u):
    for i in range(u):
        if li[i] == li[u] or u-i == abs(li[u]-li[i]):
            return False
    return True


nqueens(0)
print(result)
