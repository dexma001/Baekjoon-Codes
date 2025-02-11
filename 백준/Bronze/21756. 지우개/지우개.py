n = int(input())

temp = 0

while 2**temp <= n:
    if 2**temp == n or 2**(temp+1) > n:
        break
    temp +=1
    
print(2**temp)