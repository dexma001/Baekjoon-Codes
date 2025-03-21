answer = 0
for _ in range(int(input())):
    a,b=map(int, input().split())

    if a == 136:
        answer += 1000
    
    elif a == 142:
        answer += 5000
    
    elif a == 148:
        answer += 10000

    else:
        answer += 50000

print(answer)