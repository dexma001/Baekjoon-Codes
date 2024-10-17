# 1298

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = list(list() for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)

notebook = list(0 for _ in range(n+1))


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = True

    for j in people[i]:
        if notebook[j] == 0 or bimatch(notebook[j]):
            notebook[j] = i
            return True
    return False


for i in range(1, n+1):
    visited = list(0 for _ in range(n+1))
    bimatch(i)

answer = 0
for i in notebook:
    if i:
        answer += 1
print(answer)
