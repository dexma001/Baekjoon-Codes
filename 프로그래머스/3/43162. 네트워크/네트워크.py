from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = list(0 for _ in range(n))
    temp = deque([])
    
    for i in range(n):
        if visited[i]:
            continue
        
        temp.append(i)
        visited[i] = 1
        while temp:
            for _ in range(len(temp)):
                t = temp.popleft()
                for j in range(n):
                    if visited[j]:
                        continue
                        
                    if computers[t][j]:
                        visited[j] = 1
                        temp.append(j)
                        
        answer += 1
        
    return answer