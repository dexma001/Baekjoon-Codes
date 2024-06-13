# 7453

import sys
input = sys.stdin.readline

n = int(input())
a1 = list()
b1 = list()
c1 = list()
d1 = list()
for _ in range(n):
    a, b, c, d = map(int, input().split())
    a1.append(a)
    b1.append(b)
    c1.append(c)
    d1.append(d)

key1 = dict()

for a in a1:
    for b in b1:
        temp = a+b
        if temp not in key1.keys():
            key1[temp] = 1
        else:
            key1[temp] += 1


answer = 0
for c in c1:
    for d in d1:
        temp = -1*(c + d)
        if temp in key1.keys():
            answer += key1[temp]

print(answer)
