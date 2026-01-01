n = int(input())
answer = 0

for i in range(9, 0, -1):
    if n == 0:
        break
    
    if 1<=n<=9:
        answer += 1
        break

    if n//(i*2) >= 1:
        answer += (n//(i*2)*2)
        n %= (i*2)  

print(answer)