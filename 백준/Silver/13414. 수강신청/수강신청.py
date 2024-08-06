# 13414

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = dict()

for i in range(m):
    k = input().rstrip()
    temp[k] = i+1

answer = list(temp.items())
answer.sort(key=lambda x: x[1])

i = 0
while answer and i < n:
    k = answer.pop(0)
    print(k[0])
    i += 1
