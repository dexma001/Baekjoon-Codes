import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

answer = list(list(100 for _ in range(n+1)) for _ in range(n+1))
for i in range(1, n+1):
    answer[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    answer[a][b] = 1
    answer[b][a] = 1
    
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
                answer[j][k] = min(answer[j][k], answer[j][i] + answer[i][k])
            
temp_answer = 0
for i in range(1, n+1):
    if temp_answer == 1:
        break
    for j in range(1, n+1):
        if temp_answer == 1:
            break
        
        if i == j:
            continue
        
        if answer[i][j] > 6:
            temp_answer = 1

if temp_answer == 0:
    print("Small World! ")

else:
    print("Big World! ")