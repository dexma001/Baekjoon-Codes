#24023

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0
s = 0
e = 0

for i in range(n):
    if s < 0:
        s = i
    if m | arr[i] > m:
        temp = 0
        s = -1
        e = -1
        
    else:
        temp = arr[i] | temp
        if temp == m:
            e = i
            break
    
if temp == m:
    print(s+1, e+1)

else:
    print(-1)