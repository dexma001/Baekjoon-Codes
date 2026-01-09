answer = [0, 10000000000000]

n = int(input())
for i in range(1, n+1):
    j, m = map(int, input().split())
    
    temp = ((j - ((j-1) % (m+1)))//(m)*2+2)
    
    if temp < answer[1]:
        answer = [i, temp]
        
print(*answer)