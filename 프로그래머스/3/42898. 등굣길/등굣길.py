from collections import deque
div = 1000000007

def solution(m, n, puddles):
    mapping = list(list(1 for _ in range(m)) for _ in range(n))
    for i in puddles:
        mapping[i[1]-1][i[0]-1] = 0
        
    answer = list(list(0 for _ in range(m)) for _ in range(n))
    temp = deque([])
    temp.append([0, 0])
    answer[0][0] = 1
    
    while temp:
        for _ in range(len(temp)):
            t = temp.popleft()
            y = t[0]
            x = t[1]

            if x+1 < m and mapping[y][x+1]:
                if not answer[y][x+1]:
                    temp.append([y, x+1])
                answer[y][x+1] += answer[y][x]
                answer[y][x+1] %= div
            if y + 1 < n and mapping[y+1][x]:
                if not answer[y+1][x]:                 
                    temp.append([y+1, x])
                answer[y+1][x] += answer[y][x]
                answer[y+1][x] %= 1000000007
     
    return answer[-1][-1]