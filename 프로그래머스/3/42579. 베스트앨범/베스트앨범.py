from collections import defaultdict

def solution(genres, plays):
    temp = defaultdict(list)
    
    for i in range(len(genres)):
        if temp[genres[i]]:
            temp[genres[i]][0] += plays[i]
            temp[genres[i]][1].append([plays[i], i])
            
        else:
            temp[genres[i]].append(plays[i])
            temp[genres[i]].append(list())
            temp[genres[i]][1].append([plays[i], i])
    
    ttemp =list(temp.items())
    ttemp.sort(key=lambda x:[-x[1][0]])
    
    answer = list()
    for i in ttemp:
        t = i[1][1]
        t.sort(key=lambda x:[-x[0]])
        if len(t) < 2:
            answer.append(t[0][1])
        else:
            answer.append(t[0][1])
            answer.append(t[1][1])
            
    return answer
            