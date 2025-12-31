for _ in range(int(input())):
    temp_answer = 0
    temp_per = 0
        
    for i in range(int(input())):
        a, b = map(int, input().split())
        t = b/a
        if i == 0:
            temp_answer = b
            temp_per = t
        else:
            if t == temp_per and temp_answer > b:
                temp_answer = b
            
            elif t < temp_per:
                temp_per = t
                temp_answer = b
                
    print(temp_answer)
                