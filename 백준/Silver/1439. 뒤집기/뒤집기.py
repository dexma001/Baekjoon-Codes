import math

n=str(input())
t=0
for i in range(len(n) -1):
    if n[i] != n[i+1]:
        t += 1
        
print(math.ceil(t/2))