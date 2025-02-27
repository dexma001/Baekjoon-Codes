#2018

n = int(input())

temp = 0
answer = 0

a = 0
b = 1

while a != n:
    if temp == n:
        answer += 1
        temp += b
        b += 1
        
    else:
        if b != n:
            if temp < n:
                temp += b
                b += 1
            else:
                temp -= a
                a += 1
                
        else:
            temp -= a
            a += 1
            
print(answer + 1)