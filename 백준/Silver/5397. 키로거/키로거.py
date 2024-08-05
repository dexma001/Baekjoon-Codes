# 5397

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(str, input().rstrip()))

    left = list()
    right = list()

    for i in arr:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(right[::-1])
    print(''.join(left))
