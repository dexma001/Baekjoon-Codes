import math
import sys
input = sys.stdin.readline

a, b, d = map(int, input().split())

isprime = [True] * (b+1)
isprime[0] = False
isprime[1] = False

answer = 0
for i in range(2, b+1):
    if isprime[i] == True:
        if i >= a:
            str_i = str(i)
            if str(d) in str_i:
                answer += 1

    for j in range(i*i, b+1, i):
        isprime[j] = False

print(answer)
