#31908
import sys
input = sys.stdin.readline
from collections import defaultdict
arr = defaultdict(list)

for _ in range(int(input())):
    a,b = map(str, input().split())
    arr[b].append(a)
    
temp = list(arr.items())
answer = 0
answer_list = list()
for i, j in temp:
    if len(j) == 2 and i != "-":
        answer += 1
        answer_list.append(j)

print(answer)
for i in answer_list:
    print(*i)