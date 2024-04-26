# 5525 

import sys
input = sys.stdin.readline

n = int(input())
pn = str()

for i in range(2*n+1):
    if i % 2 == 0:
        pn += 'I'
    else:
        pn += 'O'

m = int(input())
string = str(input().rstrip())

answer = 0
for j in range(m-(2*n)):
    if string[j:j+(2*n+1)] == pn:
        answer += 1

print(answer)
