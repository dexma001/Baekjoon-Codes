# 9711

import sys
input = sys.stdin.readline

fib = [0] * 20001
fib[1] = 1
fib[2] = 1
for i in range(3, 20001):
    fib[i] = fib[i-1] + fib[i-2]

for i in range(int(input())):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i+1, fib[a] % b))
