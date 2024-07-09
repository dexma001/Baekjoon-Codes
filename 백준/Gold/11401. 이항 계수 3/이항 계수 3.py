# 13977

import sys
input = sys.stdin.readline


def mul(x, y, p):
    ans = 1
    while y > 0:
        if y % 2 != 0:
            ans *= x
            ans %= p
        x *= x
        x %= p
        y = int(y / 2)
    return ans



n, r = map(int, input().split())
p = 1000000007

ans = 1
t1 = 1
t2 = 1

for i in range(1, n+1):
        t1 *= i
        t1 %= p

for i in range(1, r+1):
        t2 *= i
        t2 %= p

for i in range(1, n-r+1):
        t2 *= i
        t2 %= p

t3 = mul(t2, p-2, p)
t3 %= p
ans = t1*t3
ans %= p
print(ans)
