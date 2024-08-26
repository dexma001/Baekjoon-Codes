# 5014

import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = list(0 for _ in range(1000001))
answer = 0
trig = 1
stack = [s]
while stack:
    for _ in range(len(stack)):
        i = stack.pop(0)
        if i == g:
            print(answer)
            quit()
        for j in (i+u, i-d):
            if 1 <= j <= f and not visited[j]:
                visited[j] = True
                stack.append(j)

    answer += 1

print('use the stairs')
