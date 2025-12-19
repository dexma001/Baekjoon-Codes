#26099

import sys
input = sys.stdin.readline

n = int(input())
answer = 1000000000000000000

for i in range(0, 5):
    if n-(3*i) >= 0 and (n-(3*i))%5 ==0:
        answer = min(answer, i+((n-(3*i))//5))

if answer == 1000000000000000000:
    print(-1)
else:
    print(answer)