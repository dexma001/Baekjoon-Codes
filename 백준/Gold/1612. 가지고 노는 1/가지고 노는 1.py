# 1612

import sys
input = sys.stdin.readline

n = int(input())
if not n % 2 or not n % 5:
    print(-1)
elif n == 1:
    print(1)
else:
    temp = 11
    answer = 2

    while temp % n:
        temp %= n
        temp *= 10
        temp += 1
        answer += 1

    print(answer)
