# 11531

from collections import defaultdict
import sys
input = sys.stdin.readline

answer = 0
penalty = 0
solved = defaultdict(int)

while True:
    try:
        a, b, c = map(str, input().split())
        if c == 'right':
            answer += 1
            penalty += int(a) + 20*solved[b]
        else:
            solved[b] += 1
    except:
        break

print(answer, penalty)
