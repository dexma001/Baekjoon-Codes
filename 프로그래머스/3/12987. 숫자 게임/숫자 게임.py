from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    
    answer = 0
    idx = 0
    for i in range(len(B)):
        if B[i] > A[idx]:
            answer += 1
            idx += 1
            
    return answer