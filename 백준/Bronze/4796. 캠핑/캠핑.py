# 4796

import sys
input = sys.stdin.readline
case = 1

while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    else:
        answer = 0
        while v >= p:
            answer += l
            v -= p
        if v < 0:
            v = 0
        answer += min(v, l)
        print(f"Case {case}: {answer}")
        case += 1
