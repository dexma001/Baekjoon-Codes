def solution(routes):
    for i in routes:
        if i[0] > i[1]:
            temp = i[1]
            i[1] = i[0]
            i[0] = temp
    routes.sort(key=lambda x:[x[1], -x[0]])

    answer = 0
    start = list()
    
    for i in routes:
        if not start:
            start = i
            answer += 1
            
        else:
            if i[0] > start[1]:
                answer += 1
                start = i

    return(answer)