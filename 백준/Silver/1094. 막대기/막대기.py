# 1094

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

while n > 0:
    if n % 2 == 1:
        answer += 1
    n //= 2

print(answer)
