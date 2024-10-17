# 2188

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cow = list(list() for _ in range(n+1))
cage = list(0 for _ in range(m+1))

for i in range(n):
    temp = list(map(int, input().split()))[1:]
    cow[i+1] = temp


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = 1

    for num in cow[i]:
        if cage[num] == 0 or bimatch(cage[num]):
            cage[num] = i
            return True
    return False


for i in range(n):
    visited = list(0 for _ in range(n+1))
    bimatch(i+1)

answer = 0
for i in cage:
    if i:
        answer += 1
print(answer)
