# 20040

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent_arr = list(i for i in range(n))

answer = 1000001


def find_root(x):
    while x != parent_arr[x]:
        x = parent_arr[x]
    return x


def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x > y:
        parent_arr[x] = y
    elif x < y:
        parent_arr[y] = x
    else:
        return


for times in range(m):
    dot_a, dot_b = map(int, input().split())
    if dot_a > dot_b:
        dot_a, dot_b = dot_b, dot_a

    if find_root(dot_a) == find_root(dot_b):
        answer = min(answer, times + 1)

    union_root(dot_a, dot_b)

print(0) if answer == 1000001 else print(answer)
