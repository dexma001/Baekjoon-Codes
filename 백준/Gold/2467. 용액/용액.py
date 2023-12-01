# 2467

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
li = list(map(int, input().split()))

x1 = 0
y1 = n - 1
value = 10e9

while x1 < y1:
    value_1 = li[x1]+li[y1]

    if abs(value_1) < value:
        x = li[x1]
        y = li[y1]
        value = abs(value_1)

    if value_1 <= 0:
        x1 += 1

    else:
        y1 -= 1

print(x, y)
