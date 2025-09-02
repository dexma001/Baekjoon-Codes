#17141

import sys
input = sys.stdin.readline
from itertools import combinations as nCr
from collections import deque

n, m = map(int, input().split())
arr = list()
virus_locate = list()
empty_place = 0

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            virus_locate.append([i, j])    
            empty_place += 1  
        elif temp[j] == 0:
            empty_place += 1      
    arr.append(temp)
    
empty_place -= m
answer = -1

possible_combinations = list(list(i) for i in nCr(virus_locate, m))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for k in range(len(possible_combinations)):
    visited = list(list(0 for _ in range(n)) for _ in range(n))
    temp = deque([])
    temp.extend(possible_combinations[k])
    for i in temp:
        visited[i[0]][i[1]] = 1
    temp_total_virus = 0
    temp_answer = 0
    while temp:
        for _ in range(len(temp)):
            p, q = temp.popleft()
            for t in range(4):
                y = p + dy[t]
                x = q + dx[t]
                if 0<=y<n and 0<=x<n and not visited[y][x]:    
                    visited[y][x] = 1
                    if arr[y][x] == 0 or arr[y][x] == 2:
                        temp_total_virus += 1
                        temp.append([y, x])
        if temp:
            temp_answer += 1
        
    if temp_total_virus == empty_place:
        if answer != -1:
            answer = min(answer, temp_answer) 
        else:
            answer = temp_answer
    
print(answer)