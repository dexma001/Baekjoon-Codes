# 1065

import math
import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for number in range(1, N+1):
    if number < 100:
        answer += 1
        continue

    elif number == 1000:
        continue

    a, b, c = map(int, list(i for i in str(number)))
    if b*2 == (a+c):
        answer += 1

print(answer)
