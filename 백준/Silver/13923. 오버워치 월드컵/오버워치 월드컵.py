from collections import defaultdict

while True:
    try:
        n = int(input())

        temp = defaultdict(list)
        
        for i in range(n):
            arr = list(map(str, input().strip()))
            for j in range(n):
                temp[arr[j]].append([i, j])
                          
        temp_list = list()
        temp_answer = ''
        for i in list(temp.keys()):
            if len(temp[i]) == 1:
                temp[i][0][0] += 1
                temp[i][0][1] += 1
                temp_list = temp[i][0]
            elif len(temp[i]) == n+1:
                for p, q in temp[i]:
                    judge = 0
                    for t in range(n):
                        if t == p:
                            continue
                        if [t, q] in temp[i]:
                            judge += 1
                    
                    for t in range(n):
                        if t == q:
                            continue
                        if [p, t] in temp[i]:
                            judge += 1
                    
                    if judge == 2:
                        temp_list = [p+1, q+1]
                
            elif len(temp[i]) == n-1:
                temp_answer = i
            else:
                continue
                
        temp_list.append(temp_answer)
        print(*temp_list)
        
    except:
        break