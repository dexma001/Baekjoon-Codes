from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
li = [i for i in range(n+1)]


def Find(u):
    if li[u] == u:
        return u
    li[u] = Find(li[u])
    return li[u]


def union(x, y):
    x = Find(x)
    y = Find(y)

    if x > y:
        li[x] = y
    else:
        li[y] = x


for _ in range(m):
    det, a, b = map(int, input().split())
    if det == 1:
        if Find(a) == Find(b):
            print('yes')
        else:
            print('no')
    else:
        union(a, b)
