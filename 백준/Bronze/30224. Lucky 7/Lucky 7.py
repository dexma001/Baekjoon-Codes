# 30224

import sys
input = sys.stdin.readline

k = str(input())

if '7' not in k:
    if int(k) % 7 == 0:
        print(1)
    else:
        print(0)
else:
    if int(k) % 7 == 0:
        print(3)
    else:
        print(2)
