from collections import deque

def dfs(n, arr, pos, m):
    temp_answer = 0
    visited = [0 for _ in range(m+1)]
    temp = deque([])
    temp.append(n)
    visited[n] = 1
    
    while temp:
        q = temp.popleft()
        for p in range(1, m+1):
            if p != n and arr[q][p] == pos and not visited[p]:
                visited[p] = 1
                temp_answer += 1
                temp.append(p)
    
    return temp_answer
    

def solution(n, results):
    answer = 0
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in results:
        arr[i[0]][i[1]] = 1
        arr[i[1]][i[0]] = -1
    
    for i in range(1, n+1):
        if dfs(i, arr, 1, n) + dfs(i, arr, -1, n) == n-1:
            answer += 1
    
    return answer