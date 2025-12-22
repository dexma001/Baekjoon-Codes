n, m = map(int, input().split())

answer = 1

for _ in range(n):
    temp = int(input())
    if temp == 0:
        answer *= 1
    else:
        answer *= temp
        
print(answer%m)
    
