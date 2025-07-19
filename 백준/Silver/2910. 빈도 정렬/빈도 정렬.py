import sys
input = sys.stdin.readline
from collections import defaultdict

n, c = map(int, input().split())
arr = list(map(int, input().split()))

temp = defaultdict(list)

for i in range(n):
    if arr[i] in temp:
        temp[arr[i]][1] += 1
    else:
        temp[arr[i]].append(i)
        temp[arr[i]].append(1)
            
answer = list(temp.items())
answer.sort(key=lambda x: [-x[1][1], x[1][0]])

answer_list = list()
for i, j in answer:
    for _ in range(j[1]):
        answer_list.append(i)
    
print(*answer_list)