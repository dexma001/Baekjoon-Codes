t = 0
for _ in range(10):
    q = int(input())
    if q == 3:
        q = -1
        
    t = (t+q) % 4
    
if t == 0:
    print('N')
elif t == 1:
    print('E')
elif t == 2: 
    print('S')
else:
    print('W')