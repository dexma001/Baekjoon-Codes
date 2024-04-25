# 9461

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


padoban_list = [0, 1, 1, 1, 2, 2] + [0] * 95


def padoban(int):
    if int <= 5:
        return padoban_list[int]
    else:
        if padoban_list[int] != 0:
            return padoban_list[int]
        else:
            padoban_list[int] = padoban(int-5) + padoban(int-1)
            return padoban_list[int]


for _ in range(int(input())):
    n = int(input())
    print(padoban(n))
