# 11402

import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())


def combination(a, b):
    k = 1
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        for i in range(1, b+1):
            k *= (a-i+1)
            k //= i
        return k


n_list = list()
k_list = list()

while n != 0 or k != 0:
    n_list.append(n % m)
    k_list.append(k % m)
    n //= m
    k //= m

ans = 1
for i in range(len(n_list)):
    ans *= combination(n_list[i], k_list[i])
    ans %= m

print(ans)
