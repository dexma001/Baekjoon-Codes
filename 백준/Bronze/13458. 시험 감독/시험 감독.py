# 13458

import math
import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in Ai:
    if i <= B:
        answer += 1
    else:
        answer += math.ceil((i-B)/C)+1

print(answer)
