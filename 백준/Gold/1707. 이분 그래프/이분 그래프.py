# 1707

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    arr = list(list() for _ in range(V+1))

    for _ in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)

    judge = list(0 for _ in range(V+1))
    answer = 'YES'

    for i in range(1, V+1):
        if judge[i]:
            continue

        judge[i] = 1
        queue = deque([i])

        while queue:
            temp = queue.popleft()
            next_judge = (judge[temp] % 2)+1
            for i in arr[temp]:
                if not judge[i]:
                    judge[i] = next_judge
                    queue.append(i)
                elif judge[i] != next_judge:
                    answer = 'NO'

    print(answer)
