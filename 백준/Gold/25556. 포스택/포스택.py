# 25556

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stacks = [[], [], [], []]

for i in arr:
    trig = True
    for j in stacks:
        if not j or j[-1] < i:
            trig = False
            j.append(i)
            break

    if trig:
        print('NO')
        break

else:
    print('YES')
