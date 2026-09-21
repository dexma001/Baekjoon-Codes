import math

def solution(n, stations, w):
    temp = list()
    for i in stations:
        temp.append([i-w, i+w])
    
    answer = 0
 
    if temp[0][0] > 1:
        answer += math.ceil(temp[0][0] /(2*w + 1))
    
    start = temp[0][0]
    end = temp[0][1]
    
    for i in range(1, len(temp)):
        if temp[i][0] > end+1:
            answer += math.ceil((temp[i][0]-1 - end)/(2*w + 1))
            start = temp[i][0]
            end = temp[i][1]
        else:
            if temp[i][1] > end:
                end = temp[i][1]
                
    answer += math.ceil((n-end)/(2*w+1))
    
    return answer