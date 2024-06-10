# 31836

import sys
input = sys.stdin.readline

n = int(input())

x = list()
y = list()

while n > 2:
    x.extend([n-1, n-2])
    y.append(n)
    n -= 3

if n == 2:
    x.append(1)
    y.append(2)

x.sort()
y.sort()

print(len(x))
print(*x)
print(len(y))
print(*y)
