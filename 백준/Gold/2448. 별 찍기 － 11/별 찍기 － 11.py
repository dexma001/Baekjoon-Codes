# 2448

import sys
input = sys.stdin.readline

n = int(input())
tri = {3: ['  *  ', ' * * ', '*****']}


def answer(n):
    if n == 3:
        return tri[3]
    else:
        if n not in tri.keys():
            a = answer(n//2)
            tri[n] = [' '*(n//2) + x + ' '*(n//2) for x in a] + \
                [x + ' ' + x for x in a]
        return tri[n]


print(*answer(n), sep='\n')
