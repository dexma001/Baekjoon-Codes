# 15824

import sys
input = sys.stdin.readline
mod = 1000000007

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0


def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    half = power(a, b//2)
    return half*half % mod if b % 2 == 0 else half*half*a % mod


for i in range(n):
    answer += arr[i]*(power(2, i) - power(2, n-i-1))
    answer %= mod

print(answer)
