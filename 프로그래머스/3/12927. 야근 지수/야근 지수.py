import heapq

def solution(n, works):
    arr = list()
    for i in works:
        heapq.heappush(arr, (-i, i))
        
    for _ in range(n):
        temp = heapq.heappop(arr)
        if temp[1] == 0:
            heapq.heappush(arr, temp)
        else:
            heapq.heappush(arr, (-(temp[1] - 1), temp[1] - 1))
    
    answer = 0
    
    for _ in range(len(works)):
        temp = heapq.heappop(arr)
        answer += (temp[1] ** 2)
    
    return answer