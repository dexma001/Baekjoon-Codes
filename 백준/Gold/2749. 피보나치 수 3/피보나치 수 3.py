# 2749

import sys
input = sys.stdin.readline

mod = 1000000
per = mod//10*15
fib = [0, 1]
for _ in range(2, per):
    fib.append((fib[-1] + fib[-2]) % mod)

print(fib[int(input()) % per])
