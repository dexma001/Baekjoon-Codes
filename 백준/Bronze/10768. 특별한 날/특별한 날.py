# 10768

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if n == 2:
    if m < 18:
        print('Before')
    elif m == 18:
        print('Special')
    else:
        print('After')
elif n == 1:
    print('Before')
else:
    print('After')
