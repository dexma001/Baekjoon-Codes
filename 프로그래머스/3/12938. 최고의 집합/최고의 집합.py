def solution(n, s):
    if n > s:
        return [-1]
    elif n == s:
        temp = list(1 for _ in range(n))
        return temp
    else:
        temp = list(s//n for _ in range(n))
        for i in range(-1, -1-(s%n), -1):
            temp[i] += 1
            
        return temp