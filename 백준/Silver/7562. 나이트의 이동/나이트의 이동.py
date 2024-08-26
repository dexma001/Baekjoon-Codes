# 2468

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    visited = list(list(0 for _ in range(n)) for _ in range(n))

    start1, start2 = map(int, input().split())
    end1, end2 = map(int, input().split())

    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    stack = list()
    stack.append([start1, start2])
    visited[start1][start2] = True
    answer = 0

    while stack:
        for _ in range(len(stack)):
            a, b = stack.pop(0)
            if a == end1 and b == end2:
                print(answer)
                break

            for i in range(8):
                x = a + dy[i]
                y = b + dx[i]

                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True
                    stack.append([x, y])

        answer += 1
