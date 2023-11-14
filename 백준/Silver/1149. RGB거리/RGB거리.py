# 1149

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
li = list(list(map(int, input().split()))for _ in range(n))
ans = list()

ans.append(li[0])

for i in range(1, n):
    add = list()
    for j in range(3):
        add.append(min([li[i][j] + ans[i-1][(j+1) % 3],
                        li[i][j] + ans[i-1][(j+2) % 3]]))
    ans.append(add)

print(min(ans[-1]))
