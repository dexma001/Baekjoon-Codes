from collections import deque, defaultdict

def solution(n, edge):
    arr = defaultdict(list)
    for i in edge:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0]) 
        
    temp = deque([])
    visited = list(0 for _ in range(n+1))
    
    temp.append(1)
    visited[1] = 1
    
    answer = 0
    tt = 0
    while temp:
        for _ in range(len(temp)):
            t = temp.popleft()
            for i in arr[t]:
                if not visited[i]:
                    visited[i] = 1
                    temp.append(i)
                    if tt:
                        answer += 1
                    else:
                        answer = 0
                        answer += 1
                        tt = 1
        
        if tt == 1:
            tt = 0
            continue
        else:
            break
            
    return answer
    