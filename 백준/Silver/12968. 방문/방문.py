r, c, k = map(int, input().split())

answer = -1

if r%2 == 1:
    if c % 2 == 1:
        if k == 1:
            answer = 1
        else:
            answer = 0
    else:
        answer = 1
else:
    answer = 1
    
print(answer) 
        