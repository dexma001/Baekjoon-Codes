import sys
sys.setrecursionlimit(10**9)

def tot(time, temp):
    temp_answer = 0
    for i in temp:
        if i > time:
            break
        temp_answer += (time // i)
    return temp_answer
    
    

def solution(n, times):
    temp = sorted(times)
    
    start = temp[0]
    end = temp[-1] * (n // len(temp))
    
    while start != end:
        mid = (start+end)//2
        t = tot(mid, temp)
        if t < n:
            start = mid + 1
        else:
            end = mid
    
    answer = end
    return answer