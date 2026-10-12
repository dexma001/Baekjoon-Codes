#AI
import heapq
from collections import deque

def solution(jobs):
    answer = 0
    time = 0
    ln = len(jobs)
        
    arr = deque(sorted([[jobs[i][1], jobs[i][0], i] for i in range(ln)], key=lambda x:x[1]))

    temp = []
    
    while arr or temp:
        while arr and arr[0][1] <= time:
            heapq.heappush(temp, arr.popleft())
            
        if temp:
            q, p, _ = heapq.heappop(temp)
            answer += time + q - p
            time += q
            
        else:
            time = arr[0][1]
        
    return (answer // ln)
    
    
    