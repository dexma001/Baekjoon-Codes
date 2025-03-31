#2740

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr_1 = list()
for _ in range(n):
    arr_1.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
arr_2 = list()
for _ in range(m):
    arr_2.append(list(map(int, input().split())))
    
answer = list(list(0 for _ in range(k)) for _ in range(n))

for i in range(n):
    for j in range(k):
        for t in range(m):
            answer[i][j] += (arr_1[i][t] * arr_2[t][j])
            
for arr in answer:
    print(*arr)