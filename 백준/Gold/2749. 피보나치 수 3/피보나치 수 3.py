# 2749

import sys
input = sys.stdin.readline

per = 1500000
fib = [0, 1]
for _ in range(2, per):
    fib.append((fib[-1] + fib[-2]) % 1000000)

print(fib[int(input()) % per])
