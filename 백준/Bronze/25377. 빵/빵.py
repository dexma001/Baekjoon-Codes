# 25377

import sys
input = sys.stdin.readline

answer = 10**9
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b < a:
        continue
    else:
        answer = min(answer, b)

print(-1) if answer == 10**9 else print(answer)
