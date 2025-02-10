import math

r,c,w=map(int, input().split())
answer = 0
r -= 1

temp = 1
for i in range(w):
    for j in range(c-1, c-1+temp):
        answer += (math.factorial(r)//(math.factorial(j)*math.factorial(r-j)))
        
    r += 1
    temp += 1
    
print(answer)