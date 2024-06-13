import sys
from collections import defaultdict
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
answer = defaultdict(int)

for i in arr:
    answer[i] += 1

temp = max(answer.values())

if n % 2 == 0:
    if temp <= n//2:
        print('YES')
    else:
        print('NO')
else:
    if temp <= (n+1)//2:
        print('YES')
    else:
        print('NO')
