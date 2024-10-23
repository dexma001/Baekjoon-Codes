# 17481

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
member = dict()
for i in range(m):
    member[str(input().rstrip())] = i

who_like = list()
for _ in range(n):
    temp = list(map(str, input().split()))[1:]
    for i in range(len(temp)):
        temp[i] = member[temp[i]]
    who_like.append(temp)

my_best = list(-1 for _ in range(m))


def bimatch(i):
    if visited[i]:
        return False
    visited[i] = 1

    for j in who_like[i]:
        if my_best[j] == -1 or bimatch(my_best[j]):
            my_best[j] = i
            return True
    return False


for i in range(n):
    visited = list(0 for _ in range(n))
    bimatch(i)

k = m - my_best.count(-1)
if k == n:
    print('YES')
else:
    print('NO')
    print(k)
