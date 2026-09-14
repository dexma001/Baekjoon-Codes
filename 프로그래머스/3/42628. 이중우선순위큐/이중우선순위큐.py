import heapq
from collections import defaultdict

def solution(operations):
    
    max_heap = list()
    min_heap = list()
    
    temp = defaultdict(int)

    for i in operations:
        a, b = i[0], i[1:]
        b = int(b)
        
        if a == "I":
            heapq.heappush(max_heap, -b)
            heapq.heappush(min_heap, b)
            temp[b] += 1
            
        else:
            if b == 1:
                while max_heap:
                    t = heapq.heappop(max_heap)
                    if temp[-t]:
                        temp[-t] -= 1
                        break
            else:
                while min_heap:
                    t = heapq.heappop(min_heap)
                    if temp[t]:
                        temp[t] -= 1
                        break
        
    answer = [0, 0]
    while max_heap:
        t = heapq.heappop(max_heap)
        if temp[-t]:
            answer[0] = -t
            break
    
    while min_heap:
        t = heapq.heappop(min_heap)
        if temp[t]:
            answer[1] = t
            break
            
    return answer