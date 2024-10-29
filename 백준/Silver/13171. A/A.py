# 13171

a = int(input())
b = int(input())
mod = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    half = power(a, b//2)
    return half*half % mod if b % 2 == 0 else half*half*a % mod


print(power(a, b))
