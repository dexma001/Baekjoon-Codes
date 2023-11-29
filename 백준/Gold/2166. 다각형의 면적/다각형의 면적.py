# 2166

import math
import sys
input = sys.stdin.readline

n = int(input())
dot_list = list()

for _ in range(n):
    dot_list.append(list(map(int, input().split())))

x1, y1 = dot_list[0]
S = 0

for i in range(n):
    x1, y1 = dot_list[(i % n)]
    x2, y2 = dot_list[((i+1) % n)]
    S += (x1*y2)-(x2*y1)

print(f'{abs(S)/2:.1f}')
