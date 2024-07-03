# 12904

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()


def bt(p):
    if len(p) == len(a):
        if p == a:
            return 1
        else:
            return 0

    if p and p[-1] == 'A':
        return bt(p[:-1])

    elif p and p[-1] == 'B':
        p = p[:-1]
        return bt(p[::-1])
    else:
        return 0


print(bt(b))
