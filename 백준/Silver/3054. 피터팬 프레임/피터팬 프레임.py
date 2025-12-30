temp = list(map(str, input().strip()))

answer = list("" for _ in range(5))

mark = ["#", "*"]
t = 0
for i in range(len(temp)):
    if (i+1)%3 == 0 and i != 0:
        t = 1
        
    for j in range(5):
        if j == 0 or j == 4:
            answer[j] += (".."+mark[t]+".")
        elif j == 1 or j == 3:
            answer[j] += ("."+mark[t]+"."+mark[t])
        else:
            if i%3 == 0 and i != 0:
                answer[j] += (mark[(t+1)%2]+"."+temp[i]+".")
            else:
                answer[j] += (mark[t]+"."+temp[i]+".")
    
    t = 0
    
if len(temp) %3 == 0:
    t = 1
    
for i in range(5):
    if i == 2:
        answer[i] += mark[t]
    else:
        answer[i] += '.'
        
for i in answer:
    print(i)