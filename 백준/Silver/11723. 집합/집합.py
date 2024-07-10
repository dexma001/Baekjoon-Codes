# 11723

import sys
input = sys.stdin.readline

s = 0

for _ in range(int(input())):
    temp = list(map(str, input().split()))
    a = temp[0]

    if a == 'add':
        s |= 1 << int(temp[1])
    elif a == 'remove':
        s &= ~(1 << int(temp[1]))
    elif a == 'toggle':
        s ^= (1 << int(temp[1]))
    elif a == 'check':
        print(1 if s & (1 << int(temp[1])) != 0 else 0)
    elif a == 'all':
        s = (1 << 21) - 1
    else:
        s = 0
