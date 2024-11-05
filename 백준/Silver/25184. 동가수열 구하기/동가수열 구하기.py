# 25184

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
    quit()

answer = list()
k = n//2

while k > 0:
    t = k + 1 - 1
    while t <= n:
        answer.append(t)
        t += n//2
    k -= 1

print(*answer)
