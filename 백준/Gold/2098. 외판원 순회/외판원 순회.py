# 2098

import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
visited_all = (1 << n) - 1
cache = [[None] * (1 << n) for _ in range(n)]
inf = 10e8


def find_path(last, visited):
    if visited == visited_all:
        return li[last][0] or inf

    if cache[last][visited] != None:
        return cache[last][visited]

    tmp = inf
    for city in range(n):
        if visited & (1 << city) == 0 and li[last][city] != 0:
            tmp = min(tmp, find_path(city, visited |
                      (1 << city)) + li[last][city])
    cache[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))
