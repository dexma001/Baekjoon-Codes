for _ in range(int(input())):
    a,b=map(str, input().split())
    a = int(a)
    
    answer =''
    for _ in range(a):
        answer += b
        
    print(answer)