# 14433

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, k1, k2 = map(int, input().split())
team1 = list(list() for _ in range(n+1))
team2 = list(list() for _ in range(n+1))

for _ in range(k1):
    a, b = map(int, input().split())
    team1[a].append(b)

for _ in range(k2):
    c, d = map(int, input().split())
    team2[c].append(d)

t1 = list(0 for _ in range(m+1))
t2 = list(0 for _ in range(m+1))

answer1 = 0
answer2 = 0


def bimatch(team, troll, i):
    if visited[i]:
        return False
    visited[i] = True

    for j in team[i]:
        if troll[j] == 0 or bimatch(team, troll, troll[j]):
            troll[j] = i
            return True
    return False


for i in range(1, n+1):
    visited = list(0 for _ in range(n+1))
    bimatch(team1, t1,  i)
for i in t1:
    if i != 0:
        answer1 += 1

for j in range(1, n+1):
    visited = list(0 for _ in range(n+1))
    bimatch(team2, t2,  j)
for j in t2:
    if j != 0:
        answer2 += 1

if answer1 < answer2:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')
